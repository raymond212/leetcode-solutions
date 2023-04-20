# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node): 
            if not node:
                return 0, 0, 0
            _, a, l_longest = dfs(node.left)
            b, _, r_longest = dfs(node.right)
            left = a + 1 if node.left else 0
            right = b + 1 if node.right else 0
            return left, right, max(left, right, l_longest, r_longest)
        
        _, _, ans = dfs(root)
        return ans