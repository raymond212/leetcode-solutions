# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # Returns max diameter, max single path length
            if not node:
                return (0, -1)

            ld, ll = dfs(node.left)
            rd, rl = dfs(node.right)

            return (max(ld, rd, 2 + ll + rl), 1 + max(ll, rl))
        return dfs(root)[0]