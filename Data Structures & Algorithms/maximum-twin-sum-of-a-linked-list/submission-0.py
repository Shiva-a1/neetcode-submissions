# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr =[]
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        r = len(arr) - 1
        l = 0
        max = 0
        while l<r:
            s = arr[l] + arr[r]
            if s > max:
                max = s
            l+=1
            r-=1
        return max