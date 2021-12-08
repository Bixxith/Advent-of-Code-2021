with open("Day-7-Input.txt") as file:
    input = file.read()
    positions = list(input.split(","))
    postionsList = list(map(int, positions))
    print(postionsList)
    

def findLowest():
    postionsList.sort()
    lowestPos = postionsList[len(postionsList)//2]
    fuelUsed = 0
    for x in range(len(postionsList)):
        if lowestPos > postionsList[x]:
            fuelUsed += lowestPos - postionsList[x]
        elif lowestPos < postionsList[x]:
            fuelUsed += postionsList[x] - lowestPos
    return fuelUsed
            
def findLowest2():
    # postionsList.sort()
    lowestPos = sum(postionsList) // len(postionsList)
    
    print(lowestPos)
    fuelUsed = 0
    
    for x in range(len(postionsList)):
        num = 0
        posDiff = 0
        if lowestPos > postionsList[x]:
            posDiff += lowestPos - postionsList[x]
        elif lowestPos < postionsList[x]:
            posDiff += postionsList[x] - lowestPos
        num = (posDiff * (posDiff + 1)) // 2
        fuelUsed += num
        
        
    return fuelUsed

print(findLowest2())