## Day 1 of Advent of Code
## Sonar Sweep
## Zach Niehoff



def SonarSweep():
    # Variables
    newData = []
    counter = 0
    # Opens the file for reading and assigns input to a variable.
    # Converts the string elements within the list to integers with
    # map so that we can do math, and then inserts them back into a list.
    with open("Day-1-Input.txt") as file:
        input = file.read()
        dataStringList = list(input.split("\n"))
        data = list(map(int, dataStringList))

    # Adds together the element and the next two elements,
    # then appends them to the newData list
    for x in range(len(data)-2):
        holderData = data[x] + data[x+1] + data[x+2]
        newData.append(holderData)    

    # Checks to see if the items increased or decreased
    for x in range(0, len(newData)):
        print(newData[x], end="")
        if int(newData[x-1]) < int(newData[x]):
            counter += 1
            print("(increased)")
        else:
            print("(decreased)")    
    return(counter)

print(SonarSweep())



