import csv

print('-=-=-= Exercício 2 -=-=-=\n')

cityList = [] 
pathList = []
with open('./cidadedistancia.csv','r',newline='') as file:
    rows = csv.reader(file)
    for row in rows:
        #formatando os erros do arquivo CSV 
        foramtedRow = row[0].split(';')
        cityList.append(foramtedRow[0])
        cityList.append(foramtedRow[2])
        formatedDistance = foramtedRow[2].split('"')
        if(len(formatedDistance) == 2):
            foramtedRow[2] = int(formatedDistance[1])
        else:
            formatedDistance2 = foramtedRow[2].split('.')
            if(formatedDistance2[0] != 'distancia'):
                foramtedRow[2] = int(formatedDistance2[0])
        pathList.append(foramtedRow)
#removendo nome das colunas 
pathList.pop(0)

print(pathList)

print('\n')