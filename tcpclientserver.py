'''
TCP Client and Server sockets
'''
import socket
import struct


class TCPClientServer:
    '''
    Creates TCP sockets for both client and server

    Messages are formatted as a fixed length value specifying the
    data length, followed by the data.

    :param data_socket: TCP socket for data transmission
    :param MSG_LENGTH_BYTES: the size in bytes to store the data length
    '''

    def __init__(self):
        self.data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.MSG_LENGTH_BYTES = 4

    def send(self, data):
        '''Send data preceeded by the length of that data'''
        length = len(data)
        self.data_socket.sendall(struct.pack('!I', length))
        self.data_socket.sendall(data.encode('utf-8'))

    def recv(self):
        '''Receive the data length followed by the actual data'''
        lengthbuf = self.recvall(self.MSG_LENGTH_BYTES)
        length, = struct.unpack('!I', lengthbuf)
        return self.recvall(length).decode('utf-8')

    def recvall(self, count):
        '''Receive data on a socket of specified length'''
        buf = b''
        while count:
            newbuf = self.data_socket.recv(count)
            if not newbuf:
                return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    def close(self, sock=None):
        '''Close the data socket or specified socket'''
        if sock is None:
            self.data_socket.close()
        else:
            sock.close()


class TCPClient(TCPClientServer):
    '''Client specific operations using TCP sockets'''

    def connect(self, host, port):
        '''Connect to the server at the specified host and port'''
        self.data_socket.connect((host, port))


class TCPServer(TCPClientServer):
    '''
    Server specific operations using TCP sockets

    :param listen_socket: TCP socket for server to listen on
    :param data_socket: TCP socket for data transmission
    :param client_ip: IPv4 address of the client that connects
    :param client_port: Port of the client that connects
    :param MAX_LISTEN: Maximum number of parallel connects to listen for
    '''

    def __init__(self):
        TCPClientServer.__init__(self)
        self.listen_socket = self.data_socket
        self.data_socket = None
        self.client_ip = None
        self.client_port = None
        self.MAX_LISTEN = 5

    def listen(self, port):
        '''Bind to the port and listen for connections'''
        self.listen_socket.bind(('', port))
        self.listen_socket.listen(self.MAX_LISTEN)

    def accept(self):
        '''Accept a connection from a client'''
        (self.data_socket, (self.client_ip, self.client_port)
         ) = self.listen_socket.accept()

    def close(self):
        '''Close the data socket at server'''
        TCPClientServer.close(self, self.data_socket)
