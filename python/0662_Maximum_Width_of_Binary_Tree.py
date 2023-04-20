# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque([(root, 1)])
        while q:
            left = q[0][1]
            right = q[-1][1]
            ans = max(ans, right - left + 1)
            for i in range(len(q)):
                node, idx = q.popleft()
                if node.left:
                    q.append((node.left, 2 * idx - 1))
                if node.right:
                    q.append((node.right, 2 * idx))
        return ans