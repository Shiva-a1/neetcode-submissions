class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)<=1:
            return len(arr)
        l, prev, length = 0, "", 0
        for r in range(1, len(arr)):
            if arr[r-1] < arr[r]:
                curr = '<'
            elif arr[r-1] > arr[r]:
                curr = '>'
            else:
                curr = ''
            if curr=="":
                l = r
            elif prev == curr:
                l = r-1
            prev = curr
            length = max(length, r-l+1)
        return length


            