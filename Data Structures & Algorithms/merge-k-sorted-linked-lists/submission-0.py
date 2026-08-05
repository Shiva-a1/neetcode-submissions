# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(left, right):
            dummy = ListNode(0)
            curr = dummy
            while left and right:
                if left.val <= right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
                curr.next = left or right
            return dummy.next


        def mergeSort(arr, s, e):
            if s == e:
                return arr[s]
            m = (s+e)//2
            left = mergeSort(arr, s, m)
            right = mergeSort(arr, m+1, e)
            return merge(left, right)
        return mergeSort(lists, 0, len(lists)-1)
               