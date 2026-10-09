# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        node_sum = 0
        def helper(root, node_sum):
            if not root:
                return False
            node_sum += root.val
            if not root.left and not root.right:
                if node_sum == targetSum:
                    return True
                return False
            if helper(root.left, node_sum):
                return True
            if helper(root.right, node_sum):
                return True
            node_sum -= root.val
            return False
        return helper(root, node_sum)
        