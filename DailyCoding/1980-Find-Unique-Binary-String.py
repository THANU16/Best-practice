class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        binary_set = set(nums)

        for i in range(2**n):
            candidate = format(i, f'0{n}b')
            if candidate not in binary_set:
                return candidate

        