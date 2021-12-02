## Day 2 of Advent of Code
## Dive!
## Zach Niehoff

def setupInput():
    
    newList = []
    with open("Day-2-Input.txt") as file:
        input = file.read()
        dataStringList = list(input.split("\n"))
    for i in range(len(dataStringList)):
        newList.append(tuple(dataStringList[i].split(' ')))   
    return newList

def dive():
    dataInput = setupInput()

    aim = 0
    horizontal = 0
    depth = 0

    for x in range(len(dataInput)):

        if dataInput[x][0] == "forward":
            horizontal += int(dataInput[x][1])
            depth += aim * int(dataInput[x][1])
        elif dataInput[x][0] == "down":
            # depth += int(dataInput[x][1]) ## used in solution 1
            aim += int(dataInput[x][1])
        elif dataInput[x][0] == "up":
            # depth -= int(dataInput[x][1])  ## used in solution 1
            aim -= int(dataInput[x][1])
        else:
            print("wtf")

    print(horizontal * depth)

ive()