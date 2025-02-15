class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(num_str, target, index=0, current_sum=0):
            if index == len(num_str):
                return current_sum == target
            
            partition_sum = 0
            for j in range(index, len(num_str)):
                partition_sum = partition_sum * 10 + int(num_str[j])
                if partition_sum + current_sum <= target and can_partition(num_str, target, j + 1, partition_sum + current_sum):
                    return True
            return False
        
        punishment_sum = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if can_partition(square_str, i):
                punishment_sum += i * i
        
        return punishment_sum