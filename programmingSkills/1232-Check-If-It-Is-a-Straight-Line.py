class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(1, len(coordinates)-1):
            if coordinates[i-1][0] == coordinates[i][0]:
                gradeint1 = "y"
            else:
                gradeint1 = (coordinates[i][1] - coordinates[i-1][1])/(coordinates[i][0] - coordinates[i-1][0])
            if coordinates[i][0] == coordinates[i+1][0]:
                gradeint2 = "y"
            else:
                gradeint2 = (coordinates[i+1][1] - coordinates[i][1])/(coordinates[i+1][0] - coordinates[i][0])
            if gradeint1 != gradeint2:
                return False
        return True
        