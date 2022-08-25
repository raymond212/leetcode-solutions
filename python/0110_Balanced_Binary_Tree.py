# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans, _ = self.helper(root)
        return ans
    
    def helper(self, node): # returns if subtree if balanced, and height of subtree
        if not node:
            return True, 0
        
        left_balance, left_h = self.helper(node.left)
        right_balance, right_h = self.helper(node.right)
        h = max(left_h, right_h) + 1

        if left_balance and right_balance and abs(left_h - right_h) <= 1:
            return True, h
        return False, h
