class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = (n * (n - 1)) // 2
        
        freq = defaultdict(int)
        good_pairs = 0
        
        for i in range(n):
            key = nums[i] - i
            good_pairs += freq[key]
            freq[key] += 1
        
        return total_pairs - good_pairs
