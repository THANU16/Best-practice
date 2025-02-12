class Solution:
    def judgeCircle(self, moves: str) -> bool:
        countR = moves.count(\R\)
        countL = moves.count(\L\)
        countU = moves.count(\U\)
        countD = moves.count(\D\)
        coordinate = (countR-countL, countU-countD)
        return True if coordinate ==(0,0) else False
        # coordinate = [0, 0]
        # for i in moves:
        #     if i == \R\:
        #         coordinate[0] += 1
        #     elif i == \L\:
        #         coordinate[0] -= 1
        #     elif i == \U\:
        #         coordinate[1] += 1
        #     else:
        #         coordinate[1] -= 1
        # if sum(coordinate) == 0:
        #     return True
        # return False
        