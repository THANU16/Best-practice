class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_count, even_count = 0, 1  # Even count starts with 1 (empty prefix sum)
        prefix_sum, result = 0, 0

        for num in arr:
            prefix_sum += num  # Update prefix sum
            if prefix_sum % 2 == 0:
                result += odd_count  # Subarrays ending here with odd sum
                even_count += 1
            else:
                result += even_count  # Subarrays ending here with odd sum
                odd_count += 1
            result %= MOD  # Keep result within MOD

        return result
