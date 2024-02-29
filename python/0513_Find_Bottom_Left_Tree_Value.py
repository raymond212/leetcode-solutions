# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # Returns height, value
            if not node:
                return 0, 0
            lh, lv = dfs(node.left)
            rh, rv = dfs(node.right)
            if lh == rh and lh == 0:
                return 1, node.val
            elif lh >= rh:
                return lh + 1, lv
            else:
                return rh + 1, rv
        
        return dfs(root)[1]