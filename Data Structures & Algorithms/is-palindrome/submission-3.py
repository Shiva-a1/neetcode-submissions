class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        s = s.lower()
        r = len(s)-1
        while l<r:
            while not s[r].isalnum() and r>l:
                r-=1
            while not s[l].isalnum() and r>l:
                l+=1
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True

