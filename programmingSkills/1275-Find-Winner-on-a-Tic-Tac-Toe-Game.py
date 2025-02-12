class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        countTable = {
            "dig1": {"A": 0, "B": 0},
            "dig2": {"A": 0, "B": 0},
            "r0": {"A": 0, "B": 0},
            "r1": {"A": 0, "B": 0},
            "r2": {"A": 0, "B": 0},
            "c0": {"A": 0, "B": 0},
            "c1": {"A": 0, "B": 0},
            "c2": {"A": 0, "B": 0}
        }
        isA = True
        for i in moves:
            row = "r"+str(i[0])
            if isA:
                countTable[row]["A"] += 1
            else:
                countTable[row]["B"] += 1
            col = "c"+str(i[1])
            if isA:
                countTable[col]["A"] += 1
            else:
                countTable[col]["B"] += 1
            if i[0] == i[1]:
                if isA:
                    countTable["dig1"]["A"] += 1
                else:
                    countTable["dig1"]["B"] += 1
            if i[0] + i[1] == 2:
                if isA:
                    countTable["dig2"]["A"] += 1
                else:
                    countTable["dig2"]["B"] += 1
            isA = not(isA)
        print(countTable)
        for key, values in countTable.items():
            for player, count in values.items():
                if count == 3:
                    return player
        if len(moves) == 9:
            return "Draw"
        return "Pending"



