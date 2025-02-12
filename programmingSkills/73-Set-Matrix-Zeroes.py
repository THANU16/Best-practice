class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        \\\
        Do not return anything, modify matrix in-place instead.
        \\\
        rowIdOfZeros = []
        columnIdOfZeros = []
        for i in range(len(matrix)):
            if 0 in  matrix[i]:
                rowIdOfZeros.append(i)
                for j, x in enumerate(matrix[i]):
                    if x == 0 and j not in columnIdOfZeros:
                        columnIdOfZeros.append(j)
        for i in rowIdOfZeros:
            matrix[i] = [0]*len(matrix[i])
        for i in columnIdOfZeros:
            for j in range(len(matrix)):
                matrix[j][i] = 0
            
        