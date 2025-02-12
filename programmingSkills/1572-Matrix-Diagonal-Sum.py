class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        width = len(mat)
        sum = 0
        for i in range(width):
            sum += mat[i][i]
            if i != width - i-1:
                sum += mat[i][width - i-1]
        return sum
            


        