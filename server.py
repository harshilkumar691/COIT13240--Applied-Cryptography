import argparse
import logging
from tcpclientserver import TCPServer
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

logger = logging.getLogger("DEMO_SERVER")

def server_protocol(server):
    def derive_key(shared_key):
        return HKDF(
            algorithm=hashes.SHA256(),
            length=32,  # AES key size is 256 bits (32 bytes)
            salt=None,
            info=b'handshake data',
            backend=default_backend()
        ).derive(shared_key)

    prompts = ["name:", "id number:", "unit name:"]
    responses = {}

    # Key derivation
    shared_key = derive_key(server.recv())

    cipher = Cipher(algorithms.AES(shared_key), modes.CTR(), backend=default_backend())
    encryptor = cipher.encryptor()
    decryptor = cipher.decryptor()

    for prompt in prompts:
        while True:
            tx_message = "PROMPT:" + prompt
            server.send(encryptor.update(tx_message.encode()))

            rx_message = decryptor.update(server.recv()).decode().strip()
            logger.debug("Received: %s", rx_message)

            if rx_message:
                responses[prompt] = rx_message
                break
            else:
                server.send(encryptor.update("PROMPT:Please enter ".encode() + prompt.encode()))

    # Write details to a file
    with open("student_details.txt", "a") as file:
        for key, value in responses.items():
            file.write(f"{key} {value}\n")

    # Send final message to client
    tx_message = f"INFO:{responses['name:']} has been added to the unit {responses['unit name:']}."
    server.send(encryptor.update(tx_message.encode()))

    return 0

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument("port", type=int, help="port of server")
    args = parser.parse_args()

    server = TCPServer()
    server.listen(args.port)

    while True:
        server.accept()
        server_protocol(server)
        server.close()
