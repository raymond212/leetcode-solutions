# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
# Iterative approach with stack
class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        result = []

        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                result.append(stack[-1].val)
        
        return result


# Morris Traversal
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []
        cur = None

        while root:
            if root.left:
                cur = root.left
                while cur.right and cur.right != root:
                    cur = cur.right
                
                if cur.right == root:
                    result.append(root.val)
                    cur.right = None
                    root = root.right
                else:
                    cur.right = root
                    root = root.left
            else:
                result.append(root.val)
                root = root.right
        
        return result

# DFS
class Solution3:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        result = []
        self.dfs(root, result)
        return result
    
    def dfs(self, node, result):
        if not node:
            return
        self.dfs(node.left, result)
        result.append(node.val)
        self.dfs(node.right, result)