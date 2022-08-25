# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.flatten_tree(root)
        return root
            
    def flatten_tree(self, node): # return most right
        if not node:
            return None

        if not node.right and not node.left:
            return node
        
        flat_left = self.flatten_tree(node.left)
        flat_right = self.flatten_tree(node.right)

        if not flat_left:
            return flat_right

        flat_left.right = node.right
        node.right = node.left
        node.left = None

        if not flat_right:
            return flat_left

        return flat_right