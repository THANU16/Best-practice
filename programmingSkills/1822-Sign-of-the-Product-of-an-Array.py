class Solution:
    def arraySign(self, nums: List[int]) -> int:
        noNeg = 0
        for i in nums:
            if i < 0:
                noNeg += 1
            if i == 0:
                return 0
        print(noNeg)
        if noNeg %2 == 0:
            return 1
        return -1
        