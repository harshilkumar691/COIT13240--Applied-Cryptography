'''
TCP server for key exchange and authenticated encryption
'''
import argparse
from tcpclientserver import TCPServer
import logging

logger = logging.getLogger("DEMO_SERVER")


def server_protocol(server):
    '''
    Process the received request and create a response
    :param server: socket used by server
    :returns: Message to be sent to client
    '''

    prompts = ["name:", "unit name:"]
    responses = []

    for prompt in prompts:
        # Send prompt to client
        tx_message = "PROMPT:" + prompt
        server.send(tx_message)

        # Receive response from client
        rx_message = server.recv()
        rx_message_fields = rx_message.split(":")
        rx_message_type = rx_message_fields[0]
        rx_message_data = rx_message_fields[1]
        logger.debug("Received: %s", rx_message)

        if rx_message_type != "RESPONSE":
            logger.error("Received unknown or incorrect message type: %s", rx_message_type)
            return 1

        responses.append(rx_message_data)

    # Send final message to client
    tx_message = f"INFO:{responses[0]} has been added to the unit {responses[1]}."
    server.send(tx_message)

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
