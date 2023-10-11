import csv
from Graph import Graph

print('\n-=-=-= Exercício 2 -=-=-=')

cityList = []
pathList = []

with open('./exercicio2/cidadedistancia.csv','r') as file:
    rows = csv.reader(file)
    # formatando os erros do arquivo CSV 
    for row in rows:
        foramtedRow = row[0].split(';')

        # formatando nome cidade partida
        if(foramtedRow[0] == 'Indiatuaba'):
            foramtedRow[0] = 'Indaiatuba'
        if(foramtedRow[0] == 'Indiatuba'):
            foramtedRow[0] = 'Indaiatuba'
        if(foramtedRow[0] == 'Indaituba'):
            foramtedRow[0] = 'Indaiatuba'
        if(foramtedRow[0] == 'Sorocaba '):
            foramtedRow[0] = 'Sorocaba'
        if(foramtedRow[0] == 'Sao Paulo '):
            foramtedRow[0] = 'Sao Paulo'
        if(foramtedRow[0] == 'Sï¿½o Paulo'):
            foramtedRow[0] = 'Sao Paulo'
        if(foramtedRow[0] == 'São Paulo'):
            foramtedRow[0] = 'Sao Paulo'
        if(foramtedRow[0] == 'Registro '):
            foramtedRow[0] = 'Registro'
        if(foramtedRow[0] == 'Osasco '):
            foramtedRow[0] = 'Osasco'

        # formatando nome cidade chegada
        if(foramtedRow[1] == 'Indiatuaba'):
            foramtedRow[1] = 'Indaiatuba'
        if(foramtedRow[1] == 'Indiatuba'):
            foramtedRow[1] = 'Indaiatuba'
        if(foramtedRow[1] == 'Indaituba'):
            foramtedRow[1] = 'Indaiatuba'
        if(foramtedRow[1] == 'Sorocaba '):
            foramtedRow[1] = 'Sorocaba'
        if(foramtedRow[1] == 'Sao Paulo '):
            foramtedRow[1] = 'Sao Paulo'
        if(foramtedRow[1] == 'Sï¿½o Paulo'):
            foramtedRow[1] = 'Sao Paulo'
        if(foramtedRow[1] == 'São Paulo'):
            foramtedRow[1] = 'Sao Paulo'
        if(foramtedRow[1] == 'Registro '):
            foramtedRow[1] = 'Registro'
        if(foramtedRow[1] == 'Osasco '):
            foramtedRow[1] = 'Osasco'

        # adicionando todas as cidades existentes em um vetor
        cityList.append(foramtedRow[0])
        cityList.append(foramtedRow[1])

        # formatando distancia entre as cidades 
        formatedDistance = foramtedRow[2].split('"')
        if(len(formatedDistance) == 2):
            foramtedRow[2] = int(formatedDistance[1])
        else:
            formatedDistance2 = foramtedRow[2].split('.')
            if(formatedDistance2[0] != 'distancia'):
                foramtedRow[2] = int(formatedDistance2[0])

        # adicionando os caminhos com suas distancias em um vetor
        pathList.append(foramtedRow)

# removendo os nomes das colunas que estão dentro dos vetores
pathList.pop(0)
cityList.pop(0)
cityList.pop(0)

# retirando cidades repitidas
uniqCityList = []
cityCheck = []
for city in cityList: 
    if city not in cityCheck:
        uniqCityList.append(city)
        cityCheck.append(city)

# criando o dicionario para gerar o grafo entre os cidades
pathDict = {}
for key in uniqCityList:
    arr = []
    for i in range(len(pathList)):
        if(key == pathList[i][0]):
            values = []
            values.append(pathList[i][1])
            values.append(pathList[i][2])
            if (values not in arr):
                arr.append(values)
        if(key == pathList[i][1]):
            values = []
            values.append(pathList[i][0])
            values.append(pathList[i][2])
            if (values not in arr):
                arr.append(values)
    pathDict[key] = arr

print('Criando dicionário a partir do arquivo CSV...')
print('\n')
for key, value in pathDict.items() :
    print ( '{ '+ f'{key}: {value} '+'}\n')

graph = Graph(pathDict)
graph.createGraphByDict()
graph.travelingSalesman()