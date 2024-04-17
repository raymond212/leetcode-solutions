# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.res = None

        def dfs(node, word):
            if not node:
                return
            word = chr(ord('a') + node.val) + word
            if not node.left and not node.right:
                if not self.res or word < self.res:
                    self.res = word
            dfs(node.left, word)
            dfs(node.right, word)
            return
        
        dfs(root, '')
        return self.res
