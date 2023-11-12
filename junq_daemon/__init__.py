from argparse import Namespace
import socket
import selectors
import os

from junq_daemon import logger
from junq_daemon import handler
# from junq_daemon import client

from junq_daemon.client import Client
from junq_daemon.tools import *




class Daemon:
    def __init__(self, args: Namespace) -> None:
        self.version = "JUNQ-Protocol v0.1a"

        self.args = args
        self.running = True

        self.logger = logger.Logger(args.verbose)
        self.handler = handler.Handler(self)

        self.sel = selectors.DefaultSelector()

        self._creaate_local()
        self._creaate_remote()

    def _creaate_remote(self):
        self.remote = socket.socket(socket.AF_INET6) # remote connection inet socket
        self.remote.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.remote.bind(("::", self.args.port))
        self.remote.listen()
        self.sel.register(self.remote, selectors.EVENT_READ, self._accept) # register remote accept event

    def _creaate_local(self):
        if os.name == "posix":
            self.local = socket.socket(socket.AF_UNIX) # local connection unix socket
            self.local.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                os.unlink(self.args.unix_path)
            except:
                if os.path.exists(self.args.unix_path):
                    raise
            self.local.bind(self.args.unix_path)
            self.local.listen()

        else: # windows, etc.
            self.local = self.remote

        self.sel.register(self.local, selectors.EVENT_READ, self._accept) # register local accept event

    def _accept(self, sock):
        conn,addr = sock.accept()
        conn.send(self.version.encode())
        self.logger.accept(conn)
        self.sel.register(conn, selectors.EVENT_READ, Client(conn, self._handle))
    
    def _handle(self, client: Client):
        self.handler.handle(client)
    
    def close(self, client: Client):
        self.sel.unregister(client.sock)
        client.sock.close()
    
    def exit(self):
        os.unlink(self.args.unix_path)
        self.handler.exit()
        self.logger.exit()
        self.local.close()
        self.remote.close()

    def loop(self):
        try:
            while self.running:
                events = self.sel.select()
                for key, _ in events:
                    if type(key.data) == Client:
                        cb = key.data.cb
                        cb(key.data)
                    else:
                        cb = key.data
                        cb(key.fileobj)
                    
        except KeyboardInterrupt:
            self.exit()
        except Exception as e:
            self.exit()
            raise e


