'''
TCP server for key exchange and authenticated encryption
'''
import argparse
from tcpclientserver import TCPServer
import logging
import os
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend

logger = logging.getLogger("DEMO_SERVER")

# Function to perform Diffie-Hellman key exchange and return the shared secret key
def diffie_hellman_key_exchange(server):
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    server_private_key = parameters.generate_private_key()
    server_public_key = server_private_key.public_key()

    server_public_key_bytes = server_public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)
    server.send(server_public_key_bytes.decode())

    client_public_key_bytes = server.recv().encode()
    client_public_key = serialization.load_pem_public_key(client_public_key_bytes, backend=default_backend())

    shared_key = server_private_key.exchange(client_public_key)
    derived_key = HKDF(algorithm=SHA256(), length=32, salt=None, info=b'handshake data', backend=default_backend()).derive(shared_key)

    return derived_key

# Function to encrypt a message using AES
def encrypt_message(key, message):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext

# Function to decrypt a message using AES
def decrypt_message(key, ciphertext):
    iv = ciphertext[:16]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    unpadder = PKCS7(algorithms.AES.block_size).unpadder()
    padded_data = decryptor.update(ciphertext[16:]) + decryptor.finalize()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()
    return plaintext.decode()

def server_protocol(server, shared_key):
    '''
    Process the received request and create a response
    :param server: socket used by server
    :param shared_key: AES key used for encryption/decryption
    :returns: Message to be sent to client
    '''

    prompts = ["name:", "id number:", "unit name:"]
    responses = {}

    for prompt in prompts:
        while True:
            # Send prompt to client
            tx_message = "PROMPT:" + prompt
            encrypted_tx_message = encrypt_message(shared_key, tx_message)
            server.send(encrypted_tx_message.hex())

            # Receive response from client
            encrypted_rx_message = bytes.fromhex(server.recv())
            rx_message = decrypt_message(shared_key, encrypted_rx_message)
            rx_message_fields = rx_message.split(":")
            rx_message_type = rx_message_fields[0]
            rx_message_data = rx_message_fields[1].strip()
            logger.debug("Received: %s", rx_message)

            if rx_message_type != "RESPONSE":
                logger.error("Received unknown or incorrect message type: %s", rx_message_type)
                return 1

            if rx_message_data:
                responses[prompt] = rx_message_data
                break
            else:
                # Notify client to enter the details for the empty field
                tx_message = "PROMPT:Please enter " + prompt
                encrypted_tx_message = encrypt_message(shared_key, tx_message)
                server.send(encrypted_tx_message.hex())

    # Append details to a file
    with open("student_details.txt", "a") as file:
        file.write(f"name: {responses['name:']}\n")
        file.write(f"id number: {responses['id number:']}\n")
        file.write(f"unit name: {responses['unit name:']}\n\n")

    # Send final message to client
    final_message = f"INFO:{responses['name:']} has been added to the unit {responses['unit name:']}."
    encrypted_final_message = encrypt_message(shared_key, final_message)
    server.send(encrypted_final_message.hex())

    return 0


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

    # The server continues forever, accepting connections from clients
    while True:
        # Blocks until client initiates a connection
        server.accept()

        # Perform Diffie-Hellman key exchange
        shared_key = diffie_hellman_key_exchange(server)

        # Process messages
        server_protocol(server, shared_key)

        # Close the data socket and wait for more clients to connect
        server.close()
