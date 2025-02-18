class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        stack = []
        num = 1

        for i, ch in enumerate(pattern):
            stack.append(num)
            num += 1

            if ch == 'I':  
                while stack:
                    result.append(str(stack.pop()))

        stack.append(num)
        while stack:
            result.append(str(stack.pop()))

        return "".join(result)
