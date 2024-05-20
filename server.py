import argparse
import logging
from tcpclientserver import TCPServer
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.kbkdf import CounterLocation
from cryptography.hazmat.primitives.kdf.kbkdf import KBKDFHMAC
from cryptography.hazmat.primitives.kdf.kbkdf import Mode
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.serialization import Encoding, ParameterFormat
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

logger = logging.getLogger("DEMO_SERVER")

def derive_key(shared_key: bytes) -> bytes:
    """Derive a secure key from the shared key using HKDF."""
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data',
    )
    return hkdf.derive(shared_key)

def encrypt_message(key, plaintext):
    """Encrypt a message using AES in CBC mode."""
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext

def decrypt_message(key, ciphertext):
    """Decrypt a message using AES in CBC mode."""
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()
    return plaintext.decode()

def server_protocol(server, key):
    details = {"name": None, "id": None, "unit": None}
    
    prompts = [("name", "Enter name:"), ("id", "Enter ID number:"), ("unit", "Enter unit name:")]

    for field, prompt in prompts:
        server.send(encrypt_message(key, prompt))
        response = decrypt_message(key, server.recv())
        if not response:
            server.send(encrypt_message(key, f"Please enter your {field}."))
            response = decrypt_message(key, server.recv())
        details[field] = response
        logger.debug(f"Received {field}: {response}")

    with open("students.txt", "a") as file:
        file.write(f"Name: {details['name']}, ID: {details['id']}, Unit: {details['unit']}\n")

    confirmation_msg = f"{details['name']} has been added to the unit {details['unit']}."
    server.send(encrypt_message(key, confirmation_msg))
    logger.debug(confirmation_msg)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("port", type=int, help="port of server")
    args = parser.parse_args()

    # Diffie-Hellman key exchange setup
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    server_private_key = parameters.generate_private_key()
    server_public_key = server_private_key.public_key()
    
    server = TCPServer()
    server.listen(args.port)
    logger.info(f"Server listening on port {args.port}")

    while True:
        server.accept()
        logger.info("Client connected.")
        
        # Send server's public key to the client
        server_public_bytes = server_public_key.public_bytes(Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
        server.send(server_public_bytes.decode())

        # Receive client's public key
        client_public_bytes = server.recv().encode()
        client_public_key = serialization.load_pem_public_key(client_public_bytes)
        
        # Generate shared key
        shared_key = server_private_key.exchange(client_public_key)
        key = derive_key(shared_key)
        
        # Handle client-server protocol
        server_protocol(server, key)
        
        server.close()
