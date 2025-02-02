class Solution:
    def isRotatedCorrectly(self, nums):
        isRotated = False
        index = 0
        for i in range(1, len(nums)):
            if nums[i-1] <= nums[i]:
                continue
            else:
                if isRotated:
                    return False, -1
                else:
                    isRotated = True
                    index = i
        return True, index

    def check(self, nums: List[int]) -> bool:
        isRotated, index = self.isRotatedCorrectly(nums)
        if not isRotated:
            return False
        else:
            tempArr = nums[index:]+ nums[:index]
            for i in range(1, len(tempArr)):
                if tempArr[i-1] <= tempArr[i]:
                    continue
                else:
                    return False
            return True
        
        

        



        