class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # number = 0
        # for i in digits:
        #     number = i +  number*10
        # number += 1

        # stack = []
        # while number != 0:
        #     stack.append(number%10)
        #     number = number //10
        # result = []
        # while len(stack) != 0:
        #     result.append(stack.pop())
        # return result
        temp = 1
        for i in range(len(digits)):
            temp = temp + digits[len(digits)-i-1]
            print(temp)
            if temp > 9:
                digits[len(digits)-i-1] = temp%10
                temp = temp//10
            else:
                digits[len(digits)-i-1] = temp
                temp = 0
                break
        if temp!= 0:
            array = [temp]
            for i in digits:
                array.append(i)
            return array
        return digits


        