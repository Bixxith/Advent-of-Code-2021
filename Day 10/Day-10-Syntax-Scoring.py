with open("Day-10-Input.txt") as file:
    rawInput = file.readlines()
    input = [line.strip() for line in rawInput]
    
openList = ['(', '{', '[', '<']
closeList = [')', '}', ']', '>']
pointTable = {')':3, ']':57,'}':1197, '>':25137}
incompleteScoreTable = {'(':1, '[':2, '{':3, '<':4}

def processLines():
    invalidLines = []
    incompleteLines = []
    illegalScore = 0
    incompleteScore = 0
    incompleteScoreList = []
    
    for i in range(len(input)):
        lineScore = checkBracketsValidity(input[i])
        if lineScore: 
            invalidLines.append(input[i])
            illegalScore += lineScore
        else:
            incompleteLines.append(input[i])
    for i in range(len(incompleteLines)):
        incompleteScoreList.append(checkIncomplete(incompleteLines[i]))
    
    incompleteScoreList.sort()
    incompleteScore = incompleteScoreList[int(len(incompleteScoreList)/2)]        
    return f'Illegal Line Score: {illegalScore} \nIncomplete Score: {incompleteScore}'
    
def checkBracketsValidity(line):
    bracketCheck = []
    for i in line:
        if i in openList:
            bracketCheck.append(i)
        elif i in closeList:
            pos = closeList.index(i)
            if ((len(bracketCheck) > 0) and (openList[pos] == bracketCheck[len(bracketCheck)-1])):
                bracketCheck.pop()
            else:
                return pointTable[i]
    return False


def checkIncomplete(line):
    bracketCheck = []
    for i in line:
        if i in openList:
            bracketCheck.append(i)
        elif i in closeList:
            pos = closeList.index(i)
            if ((len(bracketCheck) > 0) and (openList[pos] == bracketCheck[len(bracketCheck)-1])):
                bracketCheck.pop()
    return calculateIncompleteScore(bracketCheck)

def calculateIncompleteScore(brackets):
    
    bracketsToPoints = [incompleteScoreTable[x] for x in reversed(brackets)]
    score = 0

    for i in range(len(bracketsToPoints)):
        score *= 5
        score += bracketsToPoints[i]

    return score
    
print(processLines())