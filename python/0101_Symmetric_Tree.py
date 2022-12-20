# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, root.right)

    def helper(self, node1, node2):
        if node1 == node2 == None:
            return True
        if node1 == None or node2 == None:
            return False
        return node1.val == node2.val and self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)