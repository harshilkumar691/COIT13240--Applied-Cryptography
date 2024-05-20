'''
TCP client demo
'''
import argparse
from tcpclientserver import TCPClient
import logging
import os
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, load_pem_public_key
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend

logger = logging.getLogger("DEMO_CLIENT")

# Function to perform Diffie-Hellman key exchange and return the shared secret key
def diffie_hellman_key_exchange(client):
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    client_private_key = parameters.generate_private_key()
    client_public_key = client_private_key.public_key()

    client_public_key_bytes = client_public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)
    client.send(client_public_key_bytes.decode())

    server_public_key_bytes = client.recv().encode()
    server_public_key = load_pem_public_key(server_public_key_bytes, backend=default_backend())

    shared_key = client_private_key.exchange(server_public_key)
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

def client_protocol(client, shared_key):
    '''
    Sends message(s) to server and handles reply(s)
    :param client: socket used by client
    :param shared_key: AES key used for encryption/decryption
    :returns: 0 if success
    '''

    while True:
        # Receive prompt from server
        encrypted_rx_message = bytes.fromhex(client.recv())
        rx_message = decrypt_message(shared_key, encrypted_rx_message)
        rx_message_fields = rx_message.split(":")
        rx_message_type = rx_message_fields[0]
        rx_message_data = rx_message_fields[1]
        logger.debug("Received: %s", rx_message)

        if rx_message_type == "PROMPT":
            # Get user input
            user_response = input(rx_message_data + " ")

            # Send response to server
            tx_message = "RESPONSE:" + user_response
            encrypted_tx_message = encrypt_message(shared_key, tx_message)
            client.send(encrypted_tx_message.hex())

        elif rx_message_type == "INFO":
            print(rx_message_data)
            break

        else:
            logger.error("Received unknown or incorrect message type: %s", rx_message_type)
            return 1

    return 0

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

    # Perform Diffie-Hellman key exchange
    shared_key = diffie_hellman_key_exchange(client)

    # Communicate with the server
    status = client_protocol(client, shared_key)

    # Close connection to server
    client.close()
