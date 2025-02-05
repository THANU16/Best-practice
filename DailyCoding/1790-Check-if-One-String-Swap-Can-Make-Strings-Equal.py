class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        index1, index2 = 0, 0
        countDiff = 0
        for i in range(0, len(s1)):
            if s1[i] == s2[i]:
                continue
            elif countDiff == 0:
                index1 = i
                countDiff +=1
            else:
                index2 = i
                countDiff +=1
            if countDiff == 2:
                break
        if countDiff == 2:
            tempStr = ""
            for i in range (len(s2)):
                if i == index1:
                    tempStr = tempStr + s2[index2]

                elif i == index2:
                    tempStr = tempStr + s2[index1]
                else:
                    tempStr = tempStr + s2[i]
                print(tempStr)
            if s1 == tempStr:
                return True
            return False
        return False

        