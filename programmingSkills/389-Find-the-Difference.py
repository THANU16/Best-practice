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

    # def findTheDifference(self, s: str, t: str) -> str:
    #     # Initialize a dictionary to store character counts
    #     count = {}

    #     # Count characters in string t
    #     for c in t:
    #         count[c] = count.get(c, 0) + 1

    #     # Subtract counts for characters in string s
    #     for c in s:
    #         count[c] -= 1
    #         if count[c] == 0:
    #             del count[c]

    #     # The remaining character in the dictionary is the difference
    #     return list(count.keys())[0]

    def findTheDifference(self, s: str, t: str) -> str:
        diff = 0
        for i in t:
            diff += ord(i)
        for j in s:
            diff -= ord(j)
        return(chr(diff))

        
        