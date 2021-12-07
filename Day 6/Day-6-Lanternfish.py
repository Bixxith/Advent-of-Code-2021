stringConversion = ""
fishList = []
with open("Day-6-Input.txt") as file:
    input = file.readlines()
    inputList = input[0].split(',')
    
    for i in range(len(inputList)):
        fishList.append(int(inputList[i]))
        
    

for i in range(80):
    
    addFish = 0
    for timer in range(len(fishList)):
        fishList[timer] -= 1
        if fishList[timer] < 0:
            addFish += 1
            fishList[timer] = 6
    for newFish in range(addFish):
        fishList.append(8)

        
print(len(fishList))

fishLifeSpan: [] = [fishList.count(span) for span in range(9)]
for i in range(256):
    preBirth = fishLifeSpan[0]
    fishLifeSpan[:-1] = fishLifeSpan[1:]
    fishLifeSpan[6] += preBirth
    fishLifeSpan[8] = preBirth
    
print (sum(fishLifeSpan))