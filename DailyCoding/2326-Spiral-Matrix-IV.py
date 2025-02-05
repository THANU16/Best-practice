# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        direction = [(0,1), (1,0), (0,-1), (-1,0)]  #Right, Down, Left, Up
        row , col = 0, 0
        dirId = 0 
        
                
        if head == None:
            return matrix
        node = head
        while (node):
            print(row, col)
            matrix[row][col] = node.val
            node = node.next
            newRow = row + direction[dirId][0]
            newCol = col + direction[dirId][1]

            if not(0<= newRow < m and 0<= newCol < n and matrix[newRow][newCol] == -1):
                dirId = (dirId + 1) %4
                newRow = row + direction[dirId][0]
                newCol = col + direction[dirId][1]
            
            row = newRow
            col = newCol
        return matrix




        