import socket

from junq_daemon.client import Client
from junq_daemon.tools import *


class Handler:
    def __init__(self, daemon) -> None:
        self.daemon = daemon

    
    def handle(self, client: Client):
        data = client.recv()
        if data:
            match client.status: # tools.py statuses
                case 0: # type of connection
                    client._type = int(data.hex(),16)
                # case 1:
                #     print(f"1: {data}")
        self.daemon.close(client)

    def exit(self):
        print("handler exit")
        ...