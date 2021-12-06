import matplotlib.pyplot as plt
import numpy as np




inputList = []
inputDictionaryList = []
with open("Day-5-Input.txt") as file:
    for lines in file:
        inputList.append(lines.strip())
#search everything up to first comma

def createDictionary():
    commaIndex = int
    spaceIndex = int
    secondSpaceIndex = int
    secondCommaIndex = int
    
    for i in range(len(inputList)):
        inputDictionaryList.append(dict())
        commaIndex = inputList[i].index(',')
        spaceIndex = inputList[i].index(' ')
        secondSpaceIndex = inputList[i].index(' ', spaceIndex+1)
        secondCommaIndex = inputList[i].index(',', spaceIndex)
        
        inputDictionaryList[i]["x1"] = int(inputList[i][0:commaIndex])
        inputDictionaryList[i]["y1"] = int(inputList[i][commaIndex+1:spaceIndex])
        inputDictionaryList[i]["x2"] = int(inputList[i][secondSpaceIndex+1:secondCommaIndex])
        inputDictionaryList[i]["y2"] = int(inputList[i][secondCommaIndex+1:])

    return inputDictionaryList 

def plotList(input):
    for x in range(len(input)):
        plt.plot()
# plt.plot(int(inputList[0][0]), int(inputList[0][2]), linewidth=2.0)
# plt.show()       
# print(inputList)

createDictionary()

# testdictionarylist = []
# testdictionarylist.append(dict())
# testdictionarylist[0]["x1"] = 3
# print(testdictionarylist)