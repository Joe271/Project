self.potentialGraph = {
"Root": [0, 1, 2, 3, 4, 5]
0: ["0Fold", "0Bet", "0Call"],
1: ["1Fold", "1Bet", "1Call"],
2: ["2Fold", "2Bet", "2Call"],
3: ["3Fold", "3Bet", "3Call"],
4: ["4Fold", "4Bet", "4Call"],
5: ["5Fold", "5Bet", "5Call"],
6: ["6Fold", "6Bet", "6Call"],

"0Bet": [self.fold()],
"0Call": [self.fold()],
"1Bet": [self.fold()],
"2Bet": [self.fold()],

"0Fold": [self.call()],
"1Call": [self.call()],
"1Fold": [self.call()],
"2Call": [self.call()],
"3Bet": [self.call()],
"3Call": [self.call()],
"3Fold": [self.call()],
"4Bet": [self.call()],
"4Call": [self.call()],
"5Bet": [self.call()],

"2Fold": [self.computerBet()],
"4Fold": [self.computerBet()],
"5Call": [self.computerBet()],
"5Fold": [self.computerBet()],
"6Bet": [self.computerBet()],
"6Call": [self.computerBet()],
"6Fold": [self.computerBet()],

self.computerBet(): [],
self.call(): [],
self.fold(): []
}
