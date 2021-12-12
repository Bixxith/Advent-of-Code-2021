import numpy as np
with open("Day-11-Input.txt") as file:
    input = [[int(num) for num in line.strip()] for line in file.readlines()]

class OctopusFlash():
    def __init__(self, input):
        self.input = input
        self.yIndex = 0
        self.xIndex = 0
        self.flashedListLimit = 200
        self.step = 0
        self.flashCount = 0
        self.flashCheckList = []
        self.limit = 999999999999999
        self.flashedList = []
        self.regularTurn = True
        self.flashed = 0
        self.flashedinturn = 0

        
    def processFlashes(self):
        if self.flashedinturn == 100:
            print(f"All flash @ {self.step+1}")
            self.limit = self.step + 1
        if len(self.flashCheckList) > 0:
            for i in range(len(self.flashCheckList)):
                self.incrementFlash(self.flashCheckList[i])
            while len(self.flashCheckList) > 0:
                self.flashedList.append(self.flashCheckList.pop())
            self.regularTurn = False
        else:

            if len(self.flashedList) > 0:
                for i in range(len(self.flashedList)):
                    self.input[self.flashedList[i][0]][self.flashedList[i][1]] = 0 
            self.flashedList = []
            self.regularTurn = True
            self.step += 1
            self.flashedinturn = 0
            
        
            
    def incrementFlash(self, flashedCell):
        
        try:
            if flashedCell[0] >= 0 and flashedCell[1]-1 >= 0:
                self.input[flashedCell[0]][flashedCell[1]-1] += 1
        except IndexError:
            pass
        try:
            if flashedCell[0] >= 0 and flashedCell[1]+1 >= 0:
                self.input[flashedCell[0]][flashedCell[1]+1] += 1
        except IndexError:
            pass          
        try:
            if flashedCell[0]-1 >= 0 and flashedCell[1] >= 0:
                self.input[flashedCell[0]-1][flashedCell[1]] += 1
        except IndexError:
            pass        
        try:
            if flashedCell[0]+1 >= 0 and flashedCell[1] >= 0:
                self.input[flashedCell[0]+1][flashedCell[1]] += 1
        except IndexError:
            pass          
        try:
            if flashedCell[0]+1 >= 0 and flashedCell[1]-1 >= 0:
                self.input[flashedCell[0]+1][flashedCell[1]-1] += 1
        except IndexError:
            pass           
        try:
            if flashedCell[0] + 1 >= 0 and flashedCell[1] + 1 >= 0:
                self.input[flashedCell[0]+1][flashedCell[1]+1] += 1
        except IndexError:
            pass          
        try:
            if flashedCell[0]-1 >= 0 and flashedCell[1]-1 >= 0:
                self.input[flashedCell[0]-1][flashedCell[1]-1] += 1
        except IndexError:
            pass        
        try:
            if flashedCell[0]-1 >= 0 and flashedCell[1]+1 >= 0:
                self.input[flashedCell[0]-1][flashedCell[1]+1] += 1
        except IndexError:
            pass

    def processTurn(self):
        while self.step < self.limit:
            print(self.flashedinturn)   
            for y in range(len(self.input)):
                for x in range(len(self.input[y])):
                    if self.regularTurn:
                        self.input[y][x] += 1
                    if self.input[y][x] > 9 and [y,x] not in self.flashedList:
                        self.flashCheckList.append([y, x])
                        self.flashed += 1
                        self.flashedinturn += 1
                    elif [y,x] in self.flashedList:
                        pass
            self.processFlashes()



test = OctopusFlash(input)
test.processTurn()


        