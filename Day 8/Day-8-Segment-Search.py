with open("Day-8-Input.txt") as file:
    input = file.read()
    fullInputList = input.split("\n")
    
def findOutputs():
    afterDash = 0
    beforeDash = 0
    outputValues = []
    inputValues = []
    for x in range(len(fullInputList)):
       afterDash = fullInputList[x].index('|') + 2
       beforeDash = fullInputList[x].index('|') - 2
       outputValues.append(fullInputList[x][afterDash:])
       inputValues.append(fullInputList[x][:beforeDash])
    return [outputValues, inputValues]

processInput = findOutputs()

outputValues = processInput[0]
inputValues = processInput[1]



# print(signalLayout['g'])
def digits1478():
    digitCount = { '0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0 }
    for i in range(len(outputValues)):
        valuesList = outputValues[i].split(' ')
        for values in valuesList:
            digits = len(values)
            if digits == 2:
                digitCount['1'] += 1
            elif digits == 3:
                digitCount['7'] += 1
            elif digits == 4:
                digitCount['4'] += 1
            elif digits == 7:
                digitCount['8'] += 1  
    return digitCount['1'] + digitCount['7'] + digitCount['4'] + digitCount['8']

def determineOutput():
    answerList = []
    
    for i in range(len(outputValues)):
        valuesList = []
        answer = ''
        one = ''
        valuesList = outputValues[i].split(' ')
        for values in valuesList:
            letterCounts = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0}
            digits = len(values)
            if digits == 2:
               answer += '1'
               one += values
            elif digits == 3:
                answer += '7'
            elif digits == 4:
                answer += '4'
            elif digits == 7:
                answer += '8'
            elif digits == 5:
                if ('e' in values and 'g' in values) or ('a' in values and 'b' in values):
                    answer += '3'
                elif 'b' and 'f' in values:
                        answer += '5'
                else:
                    answer += '2'
                    # for each in values:
                    #     letterCounts[each] += 1
                    # if letterCounts['c'] == letterCounts['d'] == letterCounts['f'] == letterCounts['e'] == letterCounts['b']:
                    #     answer += '5'
                    # elif letterCounts['g'] == letterCounts['c'] == letterCounts['d'] == letterCounts['f'] == letterCounts['a']:
                    #     answer += '2'
                    # else:
                    #     answer += '3'

            elif digits == 6:
                if one in values:
                    answer += '9'
                else:
                    for each in values:
                        letterCounts[each] += 1
                    if letterCounts['c'] == letterCounts['a'] == letterCounts['g'] == letterCounts['e'] == letterCounts['d'] == letterCounts['b']:
                        answer += '0'
                    elif letterCounts['c'] == letterCounts['e'] == letterCounts['f'] == letterCounts['a'] == letterCounts['b'] == letterCounts['d']:
                        answer += '9'
                    else:
                        answer += '6'

        answerList.append(int(answer))   
    print(answerList)

# determineOutput()
# print(digits1478())

def decypher():
    signalLayout = {'a':'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f','g':'g'}
    for x in range(len(inputValues)):
        inputValues[x].sort()
        for items in inputValues[x]:
            signalLayout = {'a':'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f','g':'g'}
            if len(items) == 2:
                signalLayout['c'] == items[0]
                signalLayout['f'] == items[1]
            if len(items) == 3:
                for char in range(3):
                    if char !=  signalLayout['c'] or char != signalLayout['f']:
                        signalLayout['a'] == char

    
# print(inputValues)