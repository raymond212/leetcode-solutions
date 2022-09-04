# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
        
    def dfs(self, node, max_node):
        if not node:
            return 0
        good_nodes = 0
        if node.left:
            good_nodes += self.dfs(node.left, max(max_node, node.left.val))
        if node.right:
            good_nodes += self.dfs(node.right, max(max_node, node.right.val))
        if node.val >= max_node:
            good_nodes += 1
        return good_nodes