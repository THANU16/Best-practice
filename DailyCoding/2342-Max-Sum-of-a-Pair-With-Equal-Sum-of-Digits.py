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
                maxNum = max(hashTable[digitSum])
                hashTable[digitSum] = []
                hashTable[digitSum].append(maxNum)
            else:
                hashTable[digitSum] = []
                hashTable[digitSum].append(i)
        # maxPairSum = 0
        # isPairExit = False
        # # print(hashTable)
        # for key in hashTable.keys():
        #     # print(key)
        #     # if len(hashTable[key]) == 2:
        #         isPairExit = True
        #         maxPairSum = max(maxPairSum, hashTable[key][0]+hashTable[key][1])
        #     elif len(hashTable[key]) > 2:
        #         isPairExit = True
        #         # print(hashTable[key])
        #         for i in range (len(hashTable[key])-1):
        #             for j in range (i+1, len(hashTable[key])):
        #                 # print(hashTable[key][i], hashTable[key][j])
        #                 maxPairSum = max(maxPairSum,hashTable[key][i] + hashTable[key][j])
        # if not isPairExit:
        #     return -1
        return maxPairSum


# class Solution:
#     def maximumSum(self, nums: List[int]) -> int:
#         def sum_of_digits(n: int) -> int:
#             return sum(int(d) for d in str(n))  # Compute digit sum
        
#         digit_sum_map = {}  # Stores the largest number for each sum of digits
#         max_sum = -1
        
#         for num in nums:
#             digit_sum = sum_of_digits(num)
            
#             if digit_sum in digit_sum_map:
#                 # Compute the sum of the two largest numbers with this digit sum
#                 max_sum = max(max_sum, digit_sum_map[digit_sum] + num)
#                 # Update max number for this digit sum
#                 digit_sum_map[digit_sum] = max(digit_sum_map[digit_sum], num)
#             else:
#                 digit_sum_map[digit_sum] = num
        
#         return max_sum