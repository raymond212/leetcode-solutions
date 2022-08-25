# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        if not root:
            return 0
        return self.dfs(root, [], 0, target)
    
    def dfs(self, node, path, l, target):
        if not node:
            return 0
        path.append(node.val)
        temp = target
        count = 0
        for i in range(l, -1, -1):
            temp -= path[i]
            if temp == 0:
                count += 1
        count += self.dfs(node.left, path, l + 1, target)
        count += self.dfs(node.right, path, l + 1, target)
        path.pop()
        return count