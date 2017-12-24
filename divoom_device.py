import socket


class DivoomDevice:

    def __init__(self, addr):
        self.sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.addr = addr

    def connect(self):
        self.sock.connect((self.addr, 4))

    def disconnect(self):
        self.sock.close()

    def send(self, package):
        self.sock.send(bytes(package))
