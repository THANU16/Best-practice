from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = Counter(tiles)
        return self.backtrack(freq)
    
    def backtrack(self, freq):
        count = 0
        
        for char in freq:
            if freq[char] > 0:
                count += 1
                
                freq[char] -= 1
                count += self.backtrack(freq)
                freq[char] += 1
        
        return count
