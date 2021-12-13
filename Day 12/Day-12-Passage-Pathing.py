with open("Day-12-Input.txt") as file:
    input = [line.strip() for line in file.readlines()]
    print(input)




def makeDictionary(input):
    mapDictionary = dict()
    for i in range(len(input)):
        divider = input[i].index('-')
        try:
            mapDictionary[input[i][:divider]].append(input[i][divider+1:])
            if input[i][divider+1:] not in mapDictionary:
                mapDictionary[input[i][divider+1:]] = []
                mapDictionary[input[i][divider+1:]].append(input[i][:divider])
            else:
                 mapDictionary[input[i][divider+1:]].append(input[i][:divider])   
        except KeyError:
            mapDictionary[input[i][:divider]] = []
            mapDictionary[input[i][:divider]].append(input[i][divider+1:])
            if input[i][divider+1:] not in mapDictionary:
                mapDictionary[input[i][divider+1:]] = []      
                mapDictionary[input[i][divider+1:]].append(input[i][:divider])
            else:
                mapDictionary[input[i][divider+1:]].append(input[i][:divider])  
    return mapDictionary

mapDictionary = makeDictionary(input)    
visited = []
queue = []
print(mapDictionary)          
def pathCave(visited, mapDictionary, node):
    queue = []
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        # print(m, end = " ")
        
        for neighbour in mapDictionary[m]:
            # visitedCopy = visited.copy()
            # neighborMap = mapDictionary[neighbour]
            if (neighbour not in visited or neighbour == neighbour.upper()) :
                visited.append(neighbour)
                queue.append(neighbour)
            if neighbour == 'end':
                print(m, 'stop here')
                break
            # elif neighbour == 'end':
            #     queue = False
            #     break
            

            
                
                
pathCave(visited, mapDictionary, 'start')
# makeDictionary(input)