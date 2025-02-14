class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digitSum = 0
        temp = x
        while temp != 0:
            digitSum += temp%10
            temp = temp//10
        if x %digitSum == 0:
            return digitSum
        return -1
        