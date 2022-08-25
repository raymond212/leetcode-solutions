# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.dfs(1, n, {})
    
    def dfs(self, start, end, memo): # returns list of roots
        if start > end:
            return [None]
        
        if start == end:
            return [TreeNode(start)]
        
        if (start, end) in memo:
            return memo[(start, end)]
        
        roots = []
        for i in range(start, end + 1):
            left_roots = self.dfs(start, i - 1, memo)
            right_roots = self.dfs(i + 1, end, memo)
            for left_root in left_roots:
                for right_root in right_roots:
                    new_root = TreeNode(i)
                    new_root.left = left_root
                    new_root.right = right_root
                    roots.append(new_root)
                    
        memo[(start, end)] = roots
        return roots
            