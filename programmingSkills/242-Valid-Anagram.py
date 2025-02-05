class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = {}
        hashMapT = {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            keyS = s[i]
            keyT = t[i]
            if keyS in hashMapS.keys():
                hashMapS[keyS] += 1
            else:
                hashMapS[keyS] = 1
            
            if keyT in hashMapT.keys():
                hashMapT[keyT] += 1
            else:
                hashMapT[keyT] = 1


        print(hashMapS)
        print(hashMapT)
        if hashMapS == hashMapT:
            return True
        return False
        
        # for i in hashMapS.keys():
        #     if i in hashMapT.keys():
        #         if hashMapS[i] != hashMapT[i]:
        #             return False
        #     else:
        #         return False
        # return True
