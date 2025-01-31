# from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) :
        num1 = self.findNumber(l1)
        num2 = self.findNumber(l2)
        totalSum = num1 + num2
        factor = 10
        outputList = []
        outputList.append(totalSum % factor)
        totalSum //= factor
        while totalSum > 0:
            outputList.append(totalSum % factor)
            totalSum //= factor
        
        print(outputList)
        dummy = ListNode(0)
        temp = dummy
        for num in outputList:
            temp.next = ListNode(num)
            temp = temp.next
        return dummy.next

    

    def findNumber(self, l1: Optional[ListNode]) -> int:
        num = 0
        multiplyFactor = 1
        temp = l1
        while temp:
            num += temp.val * multiplyFactor
            multiplyFactor *= 10
            temp = temp.next
        return num

   


