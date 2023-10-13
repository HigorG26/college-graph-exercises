import sys 
print('-=-=-= Exercício 3 -=-=-=')

grafo = {
  'A': {'B': 5, 'C': 3, 'D': 2},
  'B': {'A': 5, 'C': 2, 'E': 4},
  'C': {'A': 3, 'B': 2, 'D': 1},
  'D': {'A': 2, 'C': 1, 'E': 7},
  'E': {'B': 4, 'D': 7}
}

arr = {v: sys.maxsize for v in grafo}
print('batata')

# for j in range(tsp):
#             checkVertex = [] 
#             totalCost = 0
#             cityPath = f'{city}'
#             totalVertexVisited = 0

#             while(totalVertexVisited != len(self.getVertex)):
#                 for x in range(len(startVertex.edgeList)):
#                     nextVertex = startVertex.edgeList[x].vertexB
#                     if nextVertex not in checkVertex:
#                         totalCost += startVertex.edgeList[x].value
#                         cityPath+=startVertex.edgeList[x].vertexB
                        
#                         if(nextVertex != city and totalVertexVisited != (len(self.getVertex)-1)):
#                             checkVertex.append(nextVertex)
#                         if(nextVertex == city and totalVertexVisited == (len(self.getVertex)-1)):
#                             checkVertex.append(nextVertex)

#                         for k in range(len(self.getVertex)):
#                             if nextVertex == self.getVertex[k].key:
#                                 startVertex = self.getVertex[k]
#                         break
#                 totalVertexVisited+=1

#             if(len(checkVertex) == len(self.getVertex)):
#                 totalCostList.append(totalCost)
#                 cityPathList.append(cityPath)        

