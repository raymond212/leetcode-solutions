# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def sum_dfs(node):
            if not node:
                return 0
            return node.val + sum_dfs(node.left) + sum_dfs(node.right)
        
        tree_sum = sum_dfs(root)

        def dfs(node):  # returns sum, res
            if not node:
                return 0, 0
            left_sum, left_res = dfs(node.left)
            right_sum, right_res = dfs(node.right)
            node_sum = left_sum + right_sum + node.val
            res = max(left_res, right_res)
            if node.left:
                res = max(res, left_sum * (tree_sum - left_sum))
            if node.right:
                res = max(res, right_sum * (tree_sum - right_sum))
            return node_sum, res
        
        _, res = dfs(root)
        return res % (10 ** 9 + 7)
