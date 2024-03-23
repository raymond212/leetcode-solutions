# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0
            if not node.left and not node.right:
                return 10 * path + node.val
            newPath = path * 10 + node.val
            return dfs(node.left, newPath) + dfs(node.right, newPath)
        
        return dfs(root, 0)
            