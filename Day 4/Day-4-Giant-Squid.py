## Day 4 of Advent of Code
## Giant Squid
## Zach Niehoff


bingoBoards = []


   
with open("Day-4-Input.txt") as file:
    i = -1
    y = -1
    input = file.readline().strip()
    bingoNumbers = input.split(",")
    for line in file:
        if line == "\n":
            i += 1
            y = -1
            bingoBoards.append([])
        else:
            holder = line.strip()
            text = holder.split(" ")
            bingoBoards[i].append([])
            y += 1
            for x in range(len(text)):
                if text[x] != "":
                    bingoBoards[i][y].append(text[x])     

    
    
    
def checkWin(bingoBoards, turn, number):
    boardNumber = 0

    for lines in bingoBoards:
        if lines[0][0] == lines[0][1] == lines[0][2] == lines[0][3] == lines[0][4]:
            if len(bingoBoards) == 1:
                countScore(bingoBoards, boardNumber, number)
            else:
                bingoBoards.pop(boardNumber)
        elif lines[0][1] == lines[1][1] == lines[2][1] == lines[3][1] == lines[4][1]:
            if len(bingoBoards) == 1:
                countScore(bingoBoards, boardNumber, number)
            else:
                bingoBoards.pop(boardNumber)
        elif lines[0][2] == lines[1][2] == lines[2][2] == lines[3][2] == lines[4][2]:
            if len(bingoBoards) == 1:
                countScore(bingoBoards, boardNumber, number)
            else:
                bingoBoards.pop(boardNumber)
        elif lines[0][3] == lines[1][3] == lines[2][3] == lines[3][3] == lines[4][3]:
            if len(bingoBoards) == 1:
                countScore(bingoBoards, boardNumber, number)
            else:
                bingoBoards.pop(boardNumber)
        elif lines[0][4] == lines[4][4] == lines[2][4] == lines[3][4] == lines[4][4]:
            if len(bingoBoards) == 1:
                countScore(bingoBoards, boardNumber, number)
            else:
                bingoBoards.pop(boardNumber)
        elif lines[1][0] == lines[1][1] == lines[1][2] == lines[1][3] == lines[1][4]:
            if len(bingoBoards) == 1:
                countScore(bingoBoards, boardNumber, number)
            else:
                bingoBoards.pop(boardNumber)
        elif lines[2][0] == lines[2][1] == lines[2][2] == lines[2][3] == lines[2][4]:
            if len(bingoBoards) == 1:
                countScore(bingoBoards, boardNumber, number)
            else:
                bingoBoards.pop(boardNumber)
        elif lines[3][0] == lines[3][1] == lines[3][2] == lines[3][3] == lines[3][4]:
            if len(bingoBoards) == 1:
                countScore(bingoBoards, boardNumber, number)
            else:
                bingoBoards.pop(boardNumber)
        elif lines[4][0] == lines[4][1] == lines[4][2] == lines[4][3] == lines[4][4]:
            if len(bingoBoards) == 1:
                countScore(bingoBoards, boardNumber, number)
            else:
                bingoBoards.pop(boardNumber)
        boardNumber += 1
    turn += 1
    if len(bingoBoards) == 1:
        countScore(bingoBoards, 0, number)
    else:    
        playTurn(turn)

def countScore(bingoBoards, boardNumber, number):
    total = 0
    for lines in bingoBoards[boardNumber]:
        for items in lines:
            if items != "*":
                total += int(items)
    print(total)
    print(total * int(number))
        
def playTurn(turn):
    checkNumbers(turn)

def startGame():
    turn = 0
    playTurn(turn)
    
def checkNumbers(turn):
    number = bingoNumbers[turn]
    boardCount = 0
    lineCount = 0
    itemCount = 0
    for boards in bingoBoards:
        for lines in boards:
            for item in lines:
                if item == number:
                    bingoBoards[boardCount][lineCount][itemCount] = "*"
                itemCount += 1
            itemCount = 0
            lineCount += 1
        lineCount = 0
        boardCount += 1
    checkWin(bingoBoards, turn, number)

startGame()

        
        