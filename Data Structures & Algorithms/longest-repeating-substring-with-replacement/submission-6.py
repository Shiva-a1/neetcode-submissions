class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # length, l = 0, 0
        # changes = k
        # mid = 0
        # r = 0
        
        # for r in range(len(s)):
        #     if s[r]!= s[l] and changes == 0:
        #         l = mid
        #         if r-l>1:
        #             changes = k - (r-l)
        #         else:
        #             changes = k
        #     if s[r]!=s[l] and changes > 0:
        #         if changes==k:
        #             mid = r
        #         changes-=1
            
        #     length = max(length, r-l+1)

        #     if r==len(s) and changes!=0:
        #         length = max(length, r-l+1+changes)
        # return length

        count = {}
        l = 0
        max_freq = 0
        length = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])
            
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            
            length = max(length, r - l + 1)
            
        return length