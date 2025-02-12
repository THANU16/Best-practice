class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
             'C': 100, 'D': 500, 'M': 1000}
    
        total = 0
        prev_value = 0

        for char in reversed(s):  # Traverse from right to left
            value = roman[char]
            if value < prev_value:  # If smaller numeral comes before a larger one
                total -= value
            else:
                total += value
            prev_value = value  # Update previous value

        return total
        