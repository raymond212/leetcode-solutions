# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {inorder[i]: i for i in range(len(inorder))}

        def dfs(start1, end1, start2, end2):
            if start1 == end1:
                return None

            val = preorder[start1]
            root = ListNode(val)
            idx = mp[val]
            leftSize = idx - start2
            rightSize = end2 - idx - 1

            root.left = dfs(start1 + 1, start1 + 1 + leftSize, start2, start2 + leftSize)
            root.right = dfs(end1 - rightSize, end1, end2 - rightSize, end2)

            return root
        
        return dfs(0, len(preorder), 0, len(inorder))