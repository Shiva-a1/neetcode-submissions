class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, length = 0, 0
        exist = {}
        for r in range(len(s)):
            if s[r] in exist:
                l = max(l, exist[s[r]] + 1)
            exist[s[r]] = r
            length = max(length, r-l + 1)
        return length
