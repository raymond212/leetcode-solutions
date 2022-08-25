# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        return self.dfs(root, 0, target)
    
    def dfs(self, node, sum, target):
        if not node:
            return False
        sum += node.val
        if not node.left and not node.right and sum == target:
            return True
        return self.dfs(node.left, sum, target) or self.dfs(node.right, sum, target)
        return False