## Day 3 of Advent of Code
## Binary Diagnostic
## Zach Niehoff


def setupInput():
    with open("Day-3-Input.txt") as file:
        input = file.read()
        dataStringList = list(input.split("\n")) 
    return dataStringList

input = setupInput()

def countBits(incremental, input=input):
    x = incremental
    zeroCount = 0
    oneCount = 0
    for each in input:
        if each[x] == "0":
            zeroCount += 1
        elif each[x] == "1":
            oneCount += 1
    return bool(zeroCount > oneCount)

def determineRating():
    oxygen = int(oxygenRating(), 2)
    scrubber = int(scrubberRating(), 2)
    print(scrubber * oxygen)
    
def oxygenRating():
    newInput = input
    incremental = 0
    oxygenBinary = ""
    for i in range(len(input[0])):
        if countBits(incremental, newInput) and len(newInput) > 1:
            oxygenBinary += "0"
            newInput = purgeInput(incremental, newInput, "0")
        elif len(newInput) > 1:
            oxygenBinary += "1"
            newInput = purgeInput(incremental, newInput, "1")
        incremental += 1
    return newInput[0]
            
def purgeInput(incremental,input, num):
    newInput = []
    for each in input:
        if each[incremental] == num:
            newInput.append(each)
    return newInput

def scrubberRating():
    newInput = input
    incremental = 0
    scrubberBinary = ""
    for i in range(len(input[0])):
        if countBits(incremental, newInput) and len(newInput) > 1:
            scrubberBinary += "1"
            newInput = purgeInput(incremental, newInput, "1")
        elif len(newInput) > 1:
            scrubberBinary += "0"
            newInput = purgeInput(incremental, newInput, "0")
        incremental += 1
    return newInput[0]

def gammaRateCalc():
    incremental = 0
    gammaRateBinary = ""
    epsilonRateBinary = ""
    for i in range(len(input[0])):
        if countBits(incremental):
            gammaRateBinary += "0"
            epsilonRateBinary += "1"
        else:
            gammaRateBinary += "1"
            epsilonRateBinary += "0"
        incremental += 1
    powerConsumption(gammaRateBinary, epsilonRateBinary)
    
def powerConsumption(gammaRateBinary, epsilonRateBinary):
    gamma = int(gammaRateBinary, 2)
    epsilon = int(epsilonRateBinary, 2)
    print(gamma * epsilon)


gammaRateCalc()
determineRating()
            
            
