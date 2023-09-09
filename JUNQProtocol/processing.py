class Handler:
    def __init__(self, ds, protocol) -> None:
        self.ds = ds
        self.protocol = protocol
    
    def handle(self, data: str):
        ...

class GlobalHandler(Handler):
    ...

class LocalHandler(Handler):
    ...