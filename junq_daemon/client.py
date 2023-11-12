import socket

from junq_daemon.tools import *

class Client:
    def __init__(self, sock:socket.socket , callback) -> None:
        self._type = 3
        self.sock = sock
        self.cb = callback
        self.status = statuses["toc"]
    
    def recv(self):
        l = self._get_length()
        if l:
            return self.sock.recv(l)
        else:
            return False

    def _get_length(self):
        l = self.sock.recv(2)
        if l:
            return int(l.hex(),16)
        else: # obfuscation or connection is closed
            return False
    
    def send(self, *args):
        msg = bytes()
        for i in args:
            if type(i) == str:
                msg += bytes(i, "ASCII")
            else:
                msg += bytes(i)
        self.sock.send(bytes(len(msg)))
        self.sock.send(msg)
