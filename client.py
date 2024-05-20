import argparse
import logging
from tcpclientserver import TCPClient
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.serialization import Encoding, ParameterFormat
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

logger = logging.getLogger("DEMO_CLIENT")

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

def client_protocol(client, key):
    while True:
        encrypted_message = client.recv()
        if not encrypted_message:
            break
        message = decrypt_message(key, encrypted_message)
        print(message)
        if message.startswith("Enter"):
            response = input()
            client.send(encrypt_message(key, response))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="IPv4 address of server")
    parser.add_argument("port", type=int, help="port of server")
    args = parser.parse_args()

    # Diffie-Hellman key exchange setup
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    client_private_key = parameters.generate_private_key()
    client_public_key = client_private_key.public_key()

    client = TCPClient()
    client.connect(args.ip, args.port)
    logger.info("Connected to server.")

    # Receive server's public key
    server_public_bytes = client.recv().encode()
    server_public_key = serialization.load_pem_public_key(server_public_bytes)

    # Send client's public key to the server
    client_public_bytes = client_public_key.public_bytes(Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
    client.send(client_public_bytes.decode())

    # Generate shared key
    shared_key = client_private_key.exchange(server_public_key)
    key = derive_key(shared_key)

    # Handle client-server protocol
    client_protocol(client, key)
    
    client.close()
