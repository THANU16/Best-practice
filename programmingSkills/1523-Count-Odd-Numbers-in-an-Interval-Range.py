class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diffrent = high - low
        # print(diffrent)
        # count = 0
        if low%2 == 0:
            if high%2 == 0:
                return diffrent//2
            return diffrent//2 + 1
            # for i in range(low+1, high+1, 2):
                # count += 1
        else:
            # for i in range(low, high+1, 2):
            #     count += 1
            return diffrent//2 + 1
        # return count

        