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
                self.getVertex[i].edgeList.append(Edge(value=valueArr[1],vertexA=key,vertexB=valueArr[0]))
                x+=1
            i+=1

    def tsp(self):
        fat = 1
        i = 2
        while i <= (len(self.getVertex)-1):
            fat *= i
            i += 1
        return round(fat/2)

    def travelingSalesman(self,city):
        tsp =  self.tsp()
        totalCostList = []
        startVertex = None

        for i in range(len(self.getVertex)):
            if city == self.getVertex[i].key:
                startVertex = self.getVertex[i]

        for j in range(tsp):
            checkVertex = [] 
            totalCost = 0
            totalVertexVisited = 1

            while(totalVertexVisited != len(self.getVertex)):
                for x in range(len(startVertex.edgeList)):
                    nextVertex = startVertex.edgeList[x].vertexB
                    totalCost += startVertex.edgeList[x].value
                    if nextVertex not in checkVertex:
                        checkVertex.append(nextVertex)
                        for k in range(len(self.getVertex)):
                            if nextVertex == self.getVertex[k].key:
                                startVertex = self.getVertex[k]
                    break
                totalVertexVisited+=1

            if(totalVertexVisited == len(self.getVertex)):
                totalCostList.append(totalCost)

        return min(totalCostList)