from Edge import Edge
from Vertex import Vertex
import sys

class Graph:
    def __init__(self, graphDict:dict = None):
        self.getGraphDict = graphDict
        if(graphDict):
            self.getVertex = [Vertex(key=key) for key in graphDict]
        else:
            self.getVertex = None

    # def createGraphByDict(self):
    #     i = 0
    #     for key in self.getGraphDict:
    #         for keyValue,value in self.getGraphDict.items():
    #             self.getVertex[i].edgeList.append(Edge(value=value,vertexA=key,vertexB=keyValue))
    #         i+=1

    def totalHamiltonCycle(self):
        fat = 1
        i = 2
        while i <= (len(self.getVertex)-1):
            fat *= i
            i += 1
        return round(fat/2)

    def checkCycle(self):
        pass

    def travelingSalesmanProblem(self,city):
        pass