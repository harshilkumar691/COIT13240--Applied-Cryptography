import argparse
import logging
from tcpclientserver import TCPServer
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

logger = logging.getLogger("DEMO_SERVER")

def server_protocol(server):
    prompts = ["name:", "id number:", "unit name:"]
    responses = {}

    # Diffie-Hellman key exchange
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    server_public_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    server.send(server_public_bytes)

    client_public_bytes = server.recv()
    client_public_key = serialization.load_pem_public_key(client_public_bytes, backend=default_backend())
    shared_key = private_key.exchange(client_public_key)

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
