# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # arr =[]
        # curr = head
        # while curr:
        #     arr.append(curr.val)
        #     curr = curr.next
        # r = len(arr) - 1
        # l = 0
        # max = 0
        # while l<r:
        #     s = arr[l] + arr[r]
        #     if s > max:
        #         max = s
        #     l+=1
        #     r-=1
        # return max

        # Another approach to solve this problem

        # Finding the mid of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing the second half of the linked list
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Finding the max twin sum
        best = 0
        left, right = head, prev
        while right:
            best = max(best, left.val + right.val)
            left = left.next
            right = right.next
        return best