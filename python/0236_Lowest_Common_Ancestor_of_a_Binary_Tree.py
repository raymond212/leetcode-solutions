# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', A: 'TreeNode', B: 'TreeNode') -> 'TreeNode':
        A_path = self.find_path(A, root, [])
        B_path = self.find_path(B, root, [])
        for i in range(min(len(A_path), len(B_path))):
            if A_path[i] == B_path[i]:
                continue
            return A_path[i - 1]
        return A_path[min(len(A_path), len(B_path)) - 1]
    
    def find_path(self, target, node, path):
        if not node:
            return None

        if node == target:
            path.append(node)
            return path
        
        if not node.left and not node.right:
            return None
        
        path.append(node)

        left = self.find_path(target, node.left, path)

        if left:
            return left

        right = self.find_path(target, node.right, path)

        if right:
            return right
        
        path.pop()
        return None