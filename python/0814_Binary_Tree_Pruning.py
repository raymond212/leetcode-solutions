# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root, contains = self.dfs(root)
        if contains:
            return root
        else:
            return None
    
    def dfs(self, node): # returns node, True if it contains 1 
        if not node:
            return None, False
        contains = False
        left, left_contains = self.dfs(node.left)
        right, right_contains = self.dfs(node.right)
        if node.val == 1 or left_contains or right_contains:
            contains = True
        if not left_contains:
            node.left = None
        if not right_contains:
            node.right = None
        return node, contains