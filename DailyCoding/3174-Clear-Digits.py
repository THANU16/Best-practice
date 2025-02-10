# class Solution:
#     def clearDigits(self, s: str) -> str:
#         stack = []
#         for char in s:
#             if char.isdigit():
#                 if stack:
#                     stack.pop()
#             else:
#                 stack.append(char)
#         deletedStr = ""
#         for i in stack:
#             deletedStr = deletedStr + i
#         return deletedStr

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(char)
       
        return "".join(stack)