class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, length = 0, 0
        exist = set()
        for r in range(len(s)):
            while s[r] in exist:
                length = max(length, r-l)
                exist.remove(s[l])
                l+=1
            exist.add(s[r])
            length = max(length, r-l + 1)
        return 1 if len(s)==1 else length

        