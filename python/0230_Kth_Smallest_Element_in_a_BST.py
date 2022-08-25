# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        self.traverse(root, nums)
        return nums[k - 1].val
    
    def traverse(self, node, nums): #index
        if node is None:
            return
        
        if not node.left and not node.right:
            nums.append(node)
            return
        
        self.traverse(node.left, nums)
        nums.append(node)
        self.traverse(node.right, nums)