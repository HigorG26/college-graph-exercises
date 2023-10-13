from Edge import Edge 
class Vertex:
    def __init__(self, key=None):
        self.key = key
        self.edgeList = None
        self.getCheck = False