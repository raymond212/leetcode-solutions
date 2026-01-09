# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None, -1
            
            left_res, left_depth = dfs(node.left)
            right_res, right_depth = dfs(node.right)

            if left_depth > right_depth:
                return left_res, left_depth + 1
            elif left_depth < right_depth:
                return right_res, right_depth + 1
            return node, left_depth + 1
        
        return dfs(root)[0]