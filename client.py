import argparse
import logging
from tcpclientserver import TCPClient
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.concatkdf import ConcatKDFHash
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

logger = logging.getLogger("DEMO_CLIENT")

def client_protocol(client, shared_key):
    '''
    Process the received prompt and send response to the server
    :param client: socket used by client
    :param shared_key: shared key for encryption/decryption
    '''
    while True:
        # Receive prompt from server
        encrypted_prompt = client.recv()
        prompt = decrypt_message(shared_key, encrypted_prompt)
        if not prompt:
            break
        print(prompt, end=" ")

        # Get user input
        response = input()

        # Send response to server
        encrypted_response = encrypt_message(shared_key, response)
        client.send(encrypted_response)

def generate_shared_key(private_key, public_key):
    '''
    Generate shared key using ECDH
    :param private_key: private key
    :param public_key: public key received from the server
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
    parser.add_argument("ip", help="IPv4 address of server")
    parser.add_argument("port", type=int, help="port of server")

    # Read and parse the command line arguments
    args = parser.parse_args()

    # Create a TCPClient object
    client = TCPClient()

    # Connect to the TCP server at the specified IP/port
    client.connect(args.ip, args.port)

    # Receive server's public key
    server_public_key = client.recv().encode()
    server_public_key = serialization.load_pem_public_key(server_public_key, default_backend())

    # Diffie-Hellman parameters setup
    parameters = ec.generate_parameters(ec.SECP384R1(), default_backend())
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()

    # Send client's public key to the server
    client_public_bytes = public_key.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
    client.send(client_public_bytes.decode())

    # Generate shared key
    shared_key = generate_shared_key(private_key, server_public_key)

    # Communicate with the server
    status = client_protocol(client, shared_key)

    # Close connection to server
    client.close()
