import numpy as np
with open("Day-9-Input.txt") as file:
    makeIntoList = [line.strip() for line in file.readlines()]
    newList = [[int(char) for char in makeIntoList[x]] for x in range(len(makeIntoList))]
    inputsMatrix = newList
    print(inputsMatrix)
    
    

def checkMatrices():
    lowestPointList = []
    for i in range(len(inputsMatrix)):
        for x in range(len(inputsMatrix[i])):
            lowestPoint = True
            if i != 0 and i != len(inputsMatrix)-1:
                if inputsMatrix[i-1][x] <= inputsMatrix[i][x]:
                    lowestPoint = False
                if inputsMatrix[i+1][x] <= inputsMatrix[i][x]:
                    lowestPoint = False
            elif i == 0:
                if inputsMatrix[i+1][x] <= inputsMatrix[i][x]:
                    lowestPoint = False
            elif i == len(inputsMatrix)-1:
                if inputsMatrix[i-1][x] <= inputsMatrix[i][x]:
                    lowestPoint = False
            if x != 0 and x != len(inputsMatrix[i])-1:
                if inputsMatrix[i][x-1] <= inputsMatrix[i][x]:
                    lowestPoint = False
                if inputsMatrix[i][x+1] <= inputsMatrix[i][x]:
                    lowestPoint = False
            elif x == 0:
                if inputsMatrix[i][x+1] <= inputsMatrix[i][x]:
                    lowestPoint = False
            elif x == len(inputsMatrix[i])-1:
                if inputsMatrix[i][x-1] <= inputsMatrix[i][x]:
                    lowestPoint = False
            if lowestPoint:
                lowestPointList.append(inputsMatrix[i][x]+1)                
    return sum(lowestPointList)

print(checkMatrices())            
