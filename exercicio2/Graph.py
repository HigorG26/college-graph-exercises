from Edge import Edge
from Vertex import Vertex

class Graph:
    def __init__(self, graphDict = None):
        self.getGraphDict = graphDict
        if(graphDict):
            self.getVertex = [Vertex(key=key) for key in graphDict]
        else:
            self.getVertex = None

    def createGraphByDict(self):
        i = 0
        for key in self.getGraphDict:
            x = 0
            for valueArr in self.getGraphDict[key]:
                self.getVertex[i].edgeList.append(Edge(value=valueArr[1],vertexA=key,vertexB=[0]))
                x+=1
            i+=1
    
    def travelingSalesman(self):
        totalPath =  self.getTotalTravelingSalesmanPath()
        valuesPath = []
        for path in range(totalPath):
            sumPath = 0
            for vertex in self.getVertex:
                for x in range(len(vertex.edgeList)):
                    if vertex.edgeList[x] == vertex.key:
                        vertex.edgeList[x].getCheck = True
            pass

    def getTotalTravelingSalesmanPath(self):
        fat = 1
        i = 2
        while i < (len(self.getVertex)-1):
            fat = fat*i
            i = i+1
        return round(fat/2)