# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if not self.check(root.right, root.val, True) or not self.check(root.left, root.val, False):
            return False
        
        return self.isValidBST(root.right) and self.isValidBST(root.left)

    def check(self, node, val, greater):
        if not node:
            return True

        if greater and node.val <= val:
            return False
        if not greater and node.val >= val:
            return False
        
        return self.check(node.left, val, greater) and self.check(node.right, val, greater)