# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = []

        def dfs(node, level):
            if not node:
                return
            if len(sums) <= level:
                sums.append(node.val)
            else:
                sums[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        print(sums)

        max_sum, idx = root.val, 0
        for i in range(1, len(sums)):
            if sums[i] > max_sum:
                idx = i 
                max_sum = sums[i]
        
        return idx + 1