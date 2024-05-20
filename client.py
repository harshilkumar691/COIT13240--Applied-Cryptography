'''
TCP client demo
'''
import argparse
from tcpclientserver import TCPClient
import logging

logger = logging.getLogger("DEMO_CLIENT")


def client_protocol(client, server_ip, server_port):
    '''
    Sends message(s) to server and handles reply(s)
    :param client: socket used by client
    :param server_ip: IPv4 address of the server (string)
    :param server_port: Port number of the server (int)
    :returns: 0 if success
    '''

    while True:
        # Receive prompt from server
        rx_message = client.recv()
        rx_message_fields = rx_message.split(":")
        rx_message_type = rx_message_fields[0]
        rx_message_data = rx_message_fields[1]
        logger.debug("Received: %s", rx_message)

        if rx_message_type == "PROMPT":
            # Get user input
            user_response = input(rx_message_data + " ")

            # Send response to server
            tx_message = "RESPONSE:" + user_response
            client.send(tx_message)
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
