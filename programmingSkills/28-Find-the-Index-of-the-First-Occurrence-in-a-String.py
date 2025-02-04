class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needlekLength = len(needle)
        for i in range(0, len(haystack)-needlekLength+1):
            if haystack[i : i+needlekLength] == needle:
                return i
        return -1