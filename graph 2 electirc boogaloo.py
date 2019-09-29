#graph 2 electic boogaloo
foldTuple = ("1Bet", "1Call", "1Fold", "2Bet", "2Call", "2Fold", "3Bet", "3Call")
callTuple = ("2Fold", "3Fold", "4Fold", "4Call", "4Bet", "5Call", "5Fold", "5Bet", "6Bet", "7Bet", "8Bet")
betTuple = ("6Call", "6Fold", "7Call", "7Fold", "8Cal", "8Fold", "9Bet", "9Call", "9Fold", "10Bet", "10Call", "10Fold")
currentGraph = {
# Each hand value: high card -> royal flush
"Root": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
# What the previous player does
1: ["1Fold", "1Bet", "1Call"],
2: ["2Fold", "2Bet", "2Call"],
3: ["3Fold", "3Bet", "3Call"],
4: ["4Fold", "4Bet", "4Call"],
5: ["5Fold", "5Bet", "5Call"],
6: ["6Fold", "6Bet", "6Call"],
7: ["7Fold", "7Bet", "7Call"],
8: ["8Fold", "8Bet", "8Call"],
9: ["9Fold", "9Bet", "9Call"],
10: ["10Fold", "10Bet", "10Call"],
# What to do
"1Bet": ["fold"],
"1Call": ["fold"],
"1Fold": ["fold"],
"2Bet": ["fold"],
"2Call": ["fold"],
"2Fold": ["fold"],
"3Bet": ["fold"],
"3Call": ["fold"],

"2Fold": ["call"],
"3Fold": ["call"],
"4Fold": ["call"],
"4Call": ["call"],
"4Bet": ["call"],
"5Call": ["call"],
"5Fold": ["call"],
"5Bet": ["call"],
"6Bet": ["call"],
"7Bet": ["call"],
"8Bet": ["call"],

"6Call": ["bet"],
"6Fold": ["bet"],
"7Call": ["bet"],
"7Fold": ["bet"],
"8Call": ["bet"],
"8Fold": ["bet"],
"9Bet": ["bet"],
"9Call": ["bet"],
"9Fold": ["bet"],
"10Bet": ["bet"],
"10Call": ["bet"],
"10Fold": ["bet"],

"bet": [],
"call": [],
"fold": []
}

def finalBfs(currentGraph, vertex):
    currentValue = 4
    currentInfoList = ["Root", currentValue, str(currentValue)+ "Fold"] # Doesnt know what the previous player did and was like where the value at
    queue = [vertex]
    moves = []
    while queue:
        currentNode = queue.pop(0)
        if currentNode in currentInfoList:
            moves.append(currentNode)
            neighbours = currentGraph[currentNode]
            for neigbour in neighbours:
                queue.append(neigbour)
        if len(moves) == 3 and neighbours == ["call"] or neighbours == ["fold"] or neighbours == ["bet"]:
            moves.extend(neighbours)
    return moves

visitedList = finalBfs(currentGraph, "Root")
print(visitedList[-1])
