class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        root = TreeNode(None)
        def TreeCreation(root, nums, i):
            if i==len(nums):
                return
            root.left = TreeNode(None)
            root.right = TreeNode(nums[i])
            TreeCreation(root.left, nums, i+1)
            TreeCreation(root.right, nums, i+1)
            return
        TreeCreation(root, nums, 0)

        big_list=[]
        def helper(root, l):
            if root.val is not None:
                l.append(root.val)
            if not root.left and not root.right:
                big_list.append(l[:])
            else:
                helper(root.left, l)
                helper(root.right, l)
            if root.val is not None:
                l.pop()
        helper(root, [])
        return big_list            