class Solution:
        
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedWord = ""
        if word1 == "":
            mergedWord += word2
            return mergedWord
        elif word2 == "":
            mergedWord += word1
            return mergedWord
        listWord1 = list(word1)
        listWord2 = list(word2)
        
        for i in range(min(len(listWord1), len(listWord2))):
            mergedWord += listWord1.pop(0)
            mergedWord += listWord2.pop(0)
        
        if len(listWord1) >0:
            for i in listWord1:
                mergedWord+=i
        else:
            for i in listWord2:
                mergedWord+=i
        
        return mergedWord

        

        