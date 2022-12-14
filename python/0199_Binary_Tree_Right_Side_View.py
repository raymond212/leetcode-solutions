# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        rightNodes = self.rightSideView(root.right)
        leftNodes = self.rightSideView(root.left)

        if len(leftNodes) > len(rightNodes):
            for i in range(len(rightNodes), len(leftNodes)):
                rightNodes.append(leftNodes[i])
        
        return [root.val] + rightNodes