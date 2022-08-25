class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        self.dfs(nums, 0, [], subsets)
        return subsets
    
    def dfs(self, nums, index, subset, subsets):
        subsets.append(list(subset))
        
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, subsets)
            subset.pop()