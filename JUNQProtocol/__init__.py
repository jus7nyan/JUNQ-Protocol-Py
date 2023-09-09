import processing
import data

class Main:
    """
    This is the main JUNQ-Protocol class.
    """
    def __init__(self) -> None:
        self.version = "0.1.0|t"
        
        self.ds = data.DataSaver(self)

        self.lprocess = processing.LocalHandler(self.ds, self)
        self.gprocess = processing.GlobalHandler(self.ds, self)

    def local_processing(self, data):
        self.lprocess.handle(data)
    
    def global_processing(self, data):
        self.gprocess.handle(data)