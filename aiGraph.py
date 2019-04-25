## AI hand graph
import pdb
opener = {
    "Root": ["HighPair", "MediumPair", "LowPair", "StrongAces", "MiddleAces", "LowSuitedAces", "SuitedPictures", "OffSuitedPic", "SuitedConnectors"],
    "HighPair": ["SBet"], # Hands
    "MediumPair": ["OFold", "OCall", "OBet"],
    "LowPair": ["OFold", "OCall", "OBet"],
    "StrongAces": ["SBet"],
    "MiddleAces": ["OFold", "OCall", "OBet"],
    "LowSuitedAces": ["OFold", "OCall", "OBet"],
    "SuitedPictures": ["OFold", "OCall", "OBet"],
    "OffSuitedPic": ["OFold", "OCall", "OBet"],
    "SuitedConnectors": ["OFold", "OCall", "OBet"],
    "OFold": ["Early", "Middle", "Small Blind"], # Opponetns action
    "OCall": ["Early", "Middle", "Small Blind"],
    "OBet": ["Early", "Middle", "Small Blind"],
    "Early": ["SBet", "SCall", "SFold"], # Table Pos
    "Middle": ["SBet", "SCall", "SFold"],
    "Small Blind": ["SBet", "SCall", "SFold"],
    "SBet": ["self.computerBet()"],
    "SCall": ["self.call()"],
    "SFold": ["self.fold()"]
}

def graph(opener, vertex):
    currentInfoList = ["Root", "MediumPair", "OFold", "Middle"]
    queue = [vertex]
    moves = []
    #pdb.set_trace()
    while queue:
        currentNode = queue.pop(0)
        if currentNode in currentInfoList:
            moves.append(currentNode)
            neighbours = opener[currentNode]
            for neighbour in neighbours:
                queue.append(neighbour)
    return moves

def bfs(opener, vertex):
    visited = []
    queue = [vertex]
    while queue:
        currentNode = queue.pop(0)
        if currentNode not in visited:
            visited.append(currentNode)
            neighbours = opener[currentNode]
            for neigbour in neighbours:
                queue.append(neigbour)
    return visited

visitedList = graph(opener, "Root")
print(visitedList)
