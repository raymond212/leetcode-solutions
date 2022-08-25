# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Iterative
class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result

# Morris Traversal
class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        nums = []
        cur = None
        
        while root:
            if root.left:
                cur = root.left
                while cur.right and cur.right != root:
                    cur = cur.right
                if cur.right == root:
                    cur.right = None
                    root = root.right
                else:
                    nums.append(root.val)
                    cur.right = root
                    root = root.left
            else:
                nums.append(root.val)
                root = root.right
                
        return nums

# DFS
class Solution3:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []
        self.dfs(root, result)
        return result
    
    def dfs(self, node, result):
        if not node:
            return
        result.append(node.val)
        self.dfs(node.left, result)
        self.dfs(node.right, result)


