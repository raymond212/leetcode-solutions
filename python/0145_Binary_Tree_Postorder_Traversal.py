# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
# Iterative approach with stack
class Solution1:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        stack = []
        prev, cur = None, root
        stack.append(root)

        while len(stack) > 0:
            cur = stack[len(stack) - 1]
            if not prev or prev.left == cur or prev.right == cur: # traverse down the tree
                if cur.left:
                    stack.append(cur.left)
                elif cur.right:
                    stack.append(cur.right)
            elif cur.left == prev: # traverse up the tree from the left
                if cur.right:
                    stack.append(cur.right)
            else: # traverse up the tree from the right
                result.append(cur.val)
                stack.pop()
            prev = cur
        
        return result

# Morris Traversal
class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        nums = []
        cur = None

        while root:
            if root.right != None:
                cur = root.right
                while cur.left and cur.left != root:
                    cur = cur.left
                if cur.left == root:
                    cur.left = None
                    root = root.left
                else:
                    nums.append(root.val)
                    cur.left = root
                    root = root.right
            else:
                nums.append(root.val)
                root = root.left
                
        nums.reverse()
        return nums

# Recursive DFS
class Solution3:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        self.dfs(root, result)
        return result
    
    def dfs(self, node, result):
        if not node:
            return
        self.dfs(node.left, result)
        self.dfs(node.right, result)
        result.append(node.val)
        return
        