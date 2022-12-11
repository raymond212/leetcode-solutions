class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        StartMax, SubtreeMax = self.helper(root)
        return max(StartMax, SubtreeMax)

    def helper(self, node): # returns maxStart, subtreeMax
        if not node:
            return 0, -float('inf')
        
        leftStartMax, leftSubtreeMax = self.helper(node.left)
        rightStartMax, rightSubtreeMax = self.helper(node.right)

        StartMax = max(node.val, node.val + leftStartMax, node.val + rightStartMax)
        SubtreeMax = max(leftSubtreeMax, rightSubtreeMax, node.val + leftStartMax + rightStartMax, StartMax)

        return StartMax, SubtreeMax