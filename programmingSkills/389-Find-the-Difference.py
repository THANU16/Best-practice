class Solution:
    # def findTheDifference(self, s: str, t: str) -> str:
    #     sArr = list(s)
    #     tArr = list(t)
    #     uniqueS = set(sArr)
    #     uniqueT = set(tArr)
    #     if len(uniqueS) != len(uniqueT):
    #         for i in uniqueT:
    #             if i not in uniqueS:
    #                 return i
    #     for i in sArr:
    #         tArr.remove(i)
    #     return tArr[0]

    def findTheDifference(self, s: str, t: str) -> str:
        diff = 0
        for i in t:
            diff += ord(i)
        for j in s:
            diff -= ord(j)
        return(chr(diff))

        
        