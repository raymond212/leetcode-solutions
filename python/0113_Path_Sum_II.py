# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        paths = []
        self.dfs(root, [], 0, target, paths)
        return paths
    
    def dfs(self, node, path, sum, target, paths):
        if not node:
            return
        sum += node.val
        path.append(node.val)
        if not node.left and not node.right and sum == target:
            paths.append(list(path))
        self.dfs(node.left, path, sum, target, paths)
        self.dfs(node.right, path, sum, target, paths)
        path.pop()