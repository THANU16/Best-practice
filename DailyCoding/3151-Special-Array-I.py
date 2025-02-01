# class Solution:
#     def isArraySpecial(self, nums: List[int]) -> bool:
#         if len(nums) <= 1:
#             return True
#         for i in range(1, len(nums)):
#             if nums[i-1] %2 == 0 and nums[i]%2 ==0:
#                 return False
#             elif nums[i-1] %2 == 1 and nums[i]%2 ==1:
#                 return False
#         return True

# # Method 2
# class Solution:
#     def isArraySpecial(self, nums: List[int]) -> bool:
#         if len(nums) <= 1:
#             return True
#         for i in range(1, len(nums)):
#             if (nums[i-1] + nums[i])%2 ==0:
#                 return False
#         return True

# Method 3
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        for i in range(1, len(nums)):
            if (nums[i-1]%2) ==  (nums[i]%2):
                return False
        return True

            

        
