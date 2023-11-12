import socket


class Logger:
    def __init__(self, verbose: int, file: str="junq.log") -> None:
        self.v = verbose
        self.file = open(file, "w+")
    
    def accept(self, conn: socket.socket):
        # print(f"accept: '{conn.getsockname()}' - '{conn.getpeername()}'")
        self.file.write(f"accept: {conn}")

    def exit(self):
        print("logger exit")
        self.file.close()