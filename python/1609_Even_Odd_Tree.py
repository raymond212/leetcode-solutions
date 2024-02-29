# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([root])
        level = 0

        while q:
            prev = None
            for _ in range(len(q)):
                node = q.popleft()
                if level % 2 == 1 and ((prev != None and node.val >= prev) or node.val % 2 == 1):
                    return False
                elif level % 2 == 0 and ((prev != None and node.val <= prev) or node.val % 2 == 0):
                    return False
                prev = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return True

