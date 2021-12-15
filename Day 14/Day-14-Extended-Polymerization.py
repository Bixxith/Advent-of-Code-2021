class Polymer():
    def __init__(self):
        self.input = self.getInput()
        self.template = self.getTemplate()
        self.insertionRules = self.getInsertionRules()
        self.steps = 10
        self.getCurrentCount()
    
    def getInput(self):
        with open("Day-14-Input.txt") as file:
            input = [lines.strip() for lines in file.readlines()]
        return input
    
    def getTemplate(self):
        template = self.input[0]
        return template
                    
    def getInsertionRules(self):
        insertionRules = dict()
        for i in range(len(self.input)):
            if i > 1:
                insertionRules[self.input[i][0:2]] = self.input[i][6]
        return insertionRules
    
    def processInsertions(self):
        newTemplate = ''
        justAdded = False
        for index in range(len(self.template)):
            
            sliceIndex = slice(index, index+2)
            polymer = self.template[sliceIndex]
    
            if polymer in self.insertionRules:
                if justAdded:
                    newTemplate += self.insertionRules[polymer] + polymer[1]
                else:
                    newTemplate += polymer[0] + self.insertionRules[polymer] + polymer[1]
                    justAdded = True
            else:
                if justAdded == False:
                    newTemplate += polymer[0]
                justAdded = False
        self.template = newTemplate

    def processResults(self):
        templateList = [char for char in self.template]
        letterSet = set(templateList)
        letterDict = dict()
        for i in letterSet:
            letterDict[i] = templateList.count(i)
        
        numberCounts = [values for values in letterDict.values()]
        numberCounts.sort()
        answer = numberCounts[len(numberCounts)-1] - numberCounts[0]
        print(answer)

    def countPairs(self):
        self.getCurrentCount()
        self.pairDict = dict()
        self.pairDictCounts = dict()
        print(self.insertionRules)
        for keys in self.insertionRules:
            self.pairDict[keys] = [keys[0] + self.insertionRules[keys], self.insertionRules[keys] + keys[1]]
            
        for values in self.pairDict.values():
            self.pairDictCounts[values[0]] = 0
            self.pairDictCounts[values[1]] = 0                                

        
    def getCurrentCount(self):
        self.currentCount = []
        for i in range(len(self.template)):
            self.currentCount.append(self.template[i] + self.template[i+1])
            
    def countPairs2(self):
        for i in range(self.currentCount):
            
    def controlProcess(self):
        counter = 0
        self.countPairs()
        # while counter < self.steps:

        #     self.processInsertions()
        #     counter += 1


        # self.processResults()
            
    
    
test = Polymer()
test.controlProcess()
# test.updateTemplate()  
# test.processInsertions()