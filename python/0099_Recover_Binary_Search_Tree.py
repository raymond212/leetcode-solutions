# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        prev = start = last = None
        
        def dfs(node):
            nonlocal prev, start, last
            if not node:
                return
            
            dfs(node.left)

            if prev and prev.val > node.val:
                if not start:
                    start = prev
                last = node
            prev = node

            dfs(node.right)

        dfs(root)
        start.val, last.val = last.val, start.val