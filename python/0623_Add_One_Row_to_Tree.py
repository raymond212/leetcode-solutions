# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node, isLeft, depth):
            if not node:
                return TreeNode(val) if depth == 1 else None
            if depth == 1:
                root = TreeNode(val)
                if isLeft:
                    root.left = node
                else:
                    root.right = node
                return root
            else:
                node.left = dfs(node.left, True, depth - 1)
                node.right = dfs(node.right, False, depth - 1)
            return node
        
        return dfs(root, True, depth)