import argparse
import logging
from tcpclientserver import TCPServer
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.concatkdf import ConcatKDFHash
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

logger = logging.getLogger("DEMO_SERVER")

def server_protocol(server, shared_key):
    '''
    Process the received request and create a response
    :param server: socket used by server
    :param shared_key: shared key for encryption/decryption
    '''

    prompts = ["name:", "id number:", "unit name:"]
    responses = {}

    for prompt in prompts:
        while True:
            # Send prompt to client
            encrypted_prompt = encrypt_message(shared_key, prompt)
            server.send(encrypted_prompt)

            # Receive response from client
            encrypted_response = server.recv()
            response = decrypt_message(shared_key, encrypted_response)
            if response:
                responses[prompt] = response
                break
            else:
                # Notify client to enter the details for the empty field
                server.send(encrypt_message(shared_key, f"Please enter {prompt}"))

    # Write details to a file
    with open("student_details.txt", "a") as file:
        for key, value in responses.items():
            file.write(f"{key} {value}\n")

    # Send final message to client
    final_message = f"{responses['name:']} has been added to the unit {responses['unit name:']}."
    encrypted_final_message = encrypt_message(shared_key, final_message)
    server.send(encrypted_final_message)

def generate_shared_key(private_key, public_key):
    '''
    Generate shared key using ECDH
    :param private_key: private key
    :param public_key: public key received from the client
    :return: shared key
    '''
    shared_key = private_key.exchange(ec.ECDH(), public_key)
    return shared_key

def encrypt_message(key, plaintext):
    '''
    Encrypt a message using AES in CBC mode
    :param key: encryption key
    :param plaintext: message to be encrypted
    :return: ciphertext
    '''
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return iv + ciphertext

def decrypt_message(key, ciphertext):
    '''
    Decrypt a message using AES in CBC mode
    :param key: decryption key
    :param ciphertext: ciphertext to be decrypted
    :return: plaintext
    '''
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext.decode()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # Read the command line arguments using argparse module
    parser = argparse.ArgumentParser()

    # Add command line arguments
    parser.add_argument("port", type=int, help="port of server")

    # Read and parse the command line arguments
    args = parser.parse_args()

    # Create a TCPServer object
    server = TCPServer()

    # Specify the port for the server to listen on
    server.listen(args.port)

    # Diffie-Hellman parameters setup
    parameters = ec.generate_parameters(ec.SECP384R1(), default_backend())
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()

    # The server continues forever, accepting connections from clients
    while True:
        # Blocks until client initiates a connection
        server.accept()
        logger.info("Client connected.")

        # Send server's public key to the client
        server_public_bytes = public_key.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
        server.send(server_public_bytes.decode())

        # Receive client's public key
        client_public_bytes = server.recv().encode()
        client_public_key = serialization.load_pem_public_key(client_public_bytes, default_backend())

        # Generate shared key
        shared_key = generate_shared_key(private_key, client_public_key)

        # Process messages
        server_protocol(server, shared_key)

        # Close the data socket and wait for more clients to connect
        server.close()
