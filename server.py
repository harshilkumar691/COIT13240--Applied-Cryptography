'''
TCP server for key exchange and authenticated encryption
'''
import argparse
from tcpclientserver import TCPServer
import logging
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

logger = logging.getLogger("DEMO_SERVER")

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

def server_protocol(server):
    # Generate server's private key
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    server_private_key = parameters.generate_private_key()
    server_public_key = server_private_key.public_key()

    # Send server's public key to client
    server_public_bytes = server_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    server.send(server_public_bytes.decode('utf-8'))

    # Receive client's public key
    client_public_bytes = server.recv()
    client_public_key = serialization.load_pem_public_key(client_public_bytes.encode('utf-8'), backend=default_backend())

    # Generate shared secret
    shared_key = server_private_key.exchange(client_public_key)
    derived_key = derive_key(shared_key)

    prompts = ["name:", "id number:", "unit name:"]
    responses = {}

    for prompt in prompts:
        while True:
            # Send prompt to client
            tx_message = encrypt_message(derived_key, "PROMPT:" + prompt)
            server.send(tx_message.hex())

            # Receive response from client
            encrypted_rx_message = bytes.fromhex(server.recv())
            rx_message = decrypt_message(derived_key, encrypted_rx_message)
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
                server.send(encrypt_message(derived_key, "PROMPT:Please enter " + prompt).hex())

    # Write details to a file
    with open("student_details.txt", "w") as file:
        for key, value in responses.items():
            file.write(f"{key} {value}\n")

    # Send final message to client
    tx_message = encrypt_message(derived_key, f"INFO:{responses['name:']} has been added to the unit {responses['unit name:']}.")
    server.send(tx_message.hex())

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

        # Process messages
        server_protocol(server)

        # Close the data socket and wait for more clients to connect
        server.close()
