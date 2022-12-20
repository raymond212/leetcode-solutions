# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, False)

    def helper(self, node, isLeft): # returns boolean and sum of left leaves
        if node == None:
            return 0
        
        leftSum = self.helper(node.left, True)
        rightSum = self.helper(node.right, False)

        totalSum = leftSum + rightSum
        if isLeft and node.left == None and node.right == None:
            totalSum += node.val

        return totalSum