import time

class Logging:
    def __init__(self, mode: str="eid", file: str="junq-protocol.log") -> None:
        """
        modes: e - err | i - info | d - debug
            set logging information
            examples: "eid", "ed", "e", "di"
        """
        self.mode = mode
        self.file = file
    
    def i(self, data):
        print(f"[INF] {data}")
    
    def e(self, data):
        print(f"[ERR] {data}")
    
    def d(self, data):
        print(f"[DBG] {data}")

    def __file_write__(self, data):
        ...