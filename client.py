'''
TCP client demo
'''
import argparse
from tcpclientserver import TCPClient
import logging
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

logger = logging.getLogger("DEMO_CLIENT")

def derive_key(shared_key):
    return HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data',
        backend=default_backend()
    ).derive(shared_key)

def encrypt_message(key, plaintext):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode('utf-8')) + encryptor.finalize()
    return iv + ciphertext

def decrypt_message(key, ciphertext):
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext.decode('utf-8')

def client_protocol(client, server_ip, server_port):
    # Receive server's public key
    server_public_bytes = client.recv()
    server_public_key = serialization.load_pem_public_key(server_public_bytes.encode('utf-8'), backend=default_backend())

    # Generate client's private key
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    client_private_key = parameters.generate_private_key()
    client_public_key = client_private_key.public_key()

    # Send client's public key to server
    client_public_bytes = client_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    client.send(client_public_bytes.decode('utf-8'))

    # Generate shared secret
    shared_key = client_private_key.exchange(server_public_key)
    derived_key = derive_key(shared_key)

    while True:
        # Receive prompt from server
        encrypted_rx_message = bytes.fromhex(client.recv())
        rx_message = decrypt_message(derived_key, encrypted_rx_message)
        rx_message_fields = rx_message.split(":")
        rx_message_type = rx_message_fields[0]
        rx_message_data = rx_message_fields[1]
        logger.debug("Received: %s", rx_message)

        if rx_message_type == "PROMPT":
            # Get user input
            user_response = input(rx_message_data + " ")

            # Send response to server
            tx_message = encrypt_message(derived_key, "RESPONSE:" + user_response)
            client.send(tx_message.hex())
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

    # Communicate with the server
    status = client_protocol(client, args.ip, args.port)

    # Close connection to server
    client.close()
