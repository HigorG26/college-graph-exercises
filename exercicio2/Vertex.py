from Edge import Edge 
class Vertex:
    def __init__(self, key=None):
        self.key = key
        self.edgeList = []
        self.getCheck = False
    
    def createEdgeList(graphDict):
        i = 0
        for key in self.getGraphDict:
            x = 0
            for valueArr in self.getGraphDict[key]:
                self.getVertex[i].edgeList.append(Edge(value=valueArr[1],vertexA=key,vertexB=[0]))
                x+=1
            i+=1