# class Solution:
#     def lemonadeChange(self, bills: List[int]) -> bool:
#         coinBank = {5:0, 10:0, 20:0}
#         for i in bills:
#             if i == 5:
#                 coinBank[5] += 1
#                 continue
#             elif i == 10:
#                 if coinBank[5] != 0:
#                     coinBank[5] -= 1
#                     coinBank[10] += 1
#                     continue
#                 else:
#                     return False
#             else:
#                 if coinBank[5] != 0 and coinBank[10] !=0:
#                     coinBank[10] -= 1
#                     coinBank[5] -= 1
#                     coinBank[20] +=1
#                 elif coinBank[5] >=3:
#                     coinBank[5] -= 3
#                     coinBank[20] +=1
#                 else:
#                     return False
#         return True

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coinFive = 0
        coinTen = 0
        for i in bills:
            if i == 5:
                coinFive += 1
                continue
            elif i == 10:
                if coinFive != 0:
                    coinFive -= 1
                    coinTen += 1
                    continue
                else:
                    return False
            else:
                if coinFive != 0 and coinTen !=0:
                    coinTen -= 1
                    coinFive -= 1
                elif coinFive >=3:
                    coinFive -= 3
                else:
                    return False
        return True

        