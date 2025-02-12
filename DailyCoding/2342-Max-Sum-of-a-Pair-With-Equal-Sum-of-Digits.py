class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hashTable = {}
        maxPairSum = -1
        for i in nums:
            digitSum = 0
            temp = i
            while temp != 0:
                digitSum += temp%10
                temp = temp//10
            
            if digitSum in hashTable.keys():
                maxPairSum = max(maxPairSum, i + max(hashTable[digitSum]))
                hashTable[digitSum].append(i)
                hashTable[digitSum] = [max(hashTable[digitSum])]
            else:
                hashTable[digitSum] = []
                hashTable[digitSum].append(i)
        return maxPairSum