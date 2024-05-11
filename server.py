'''
TCP server for kex exchange and authenticated encryption
'''
import argparse
import logging

logger = logging.getLogger("DEMO_SERVER")


def server_protocol(server):
    '''
    Process the received request and create a response
    :param server: socket used by server
    :returns: Message to be sent to client
    '''

    message_to_receive = True
    while message_to_receive:

        # Pre-process received message
        rx_message = server.recv()
        rx_message_fields = rx_message.split(":")
        rx_message_type = rx_message_fields[0]
        rx_message_data = rx_message_fields[1]
        logger.debug("Received: %s", rx_message)
        
        # Check message type and process
        if rx_message_type == "101":
            tx_message_type = "201"
            tx_message_data = "Thank you for the 1st message."            
            
        elif rx_message_type == "102":
            tx_message_type = "202"
            tx_message_data = "Good bye"
            message_to_receive = False
            
        else:
            logger.error(
                "Received unknown or incorrect message type: %s",
                rx_message_type)
            message_to_receive = False
            return 1

        # Send response
        tx_message = tx_message_type + ":" + tx_message_data
        server.send(tx_message)

    # End while

    return 0


if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG)

    # Read the command line arguments using argparse module
    parser = argparse.ArgumentParser()

    # Add command line arguments
    parser.add_argument("port", type=int,
                        help="port of server")

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
