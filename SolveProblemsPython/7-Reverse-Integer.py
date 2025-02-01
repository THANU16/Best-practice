# class Solution:
#     def reverse(self, x: int) -> int:
#         if x < (2**31) -1  and x > (-1) * (2**31):
#             reverseInt = 0
#             isNeg = False
#             if x <0:
#                 isNeg =True
#                 x = x * (-1)
#             while x > 0:
#                 reverseInt = reverseInt*10 + (x%10)
#                 x = x//10
#             if isNeg:
#                 return (-1) * reverseInt
#             return reverseInt
#         else:
#             return 0
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if x < 0:
            res = int(str(x)[1:][::-1]) * -1
        else:
            res = int(str(x)[::-1])
        
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        
        return res