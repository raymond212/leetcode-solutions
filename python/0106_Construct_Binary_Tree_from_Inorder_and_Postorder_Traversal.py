# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mp = {inorder[i]: i for i in range(len(inorder))}

        def dfs(start1, end1, start2, end2):
            if start1 == end1:
                return None

            val = postorder[end1 - 1]
            root = ListNode(val)
            idx = mp[val]
            leftSize = idx - start2
            rightSize = end2 - idx - 1

            root.left = dfs(start1, start1 + leftSize, start2, start2 + leftSize)
            root.right = dfs(end1 - rightSize - 1, end1 - 1, end2 - rightSize, end2)

            return root
        
        return dfs(0, len(postorder), 0, len(inorder))