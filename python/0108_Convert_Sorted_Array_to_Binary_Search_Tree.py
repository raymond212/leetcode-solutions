# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums) - 1)
        
    def helper(self, nums, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(nums[start])
        mid = (start + end) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, start, mid - 1)
        node.right = self.helper(nums, mid + 1, end)
        return node