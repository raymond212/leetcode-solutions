class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        nums.sort()
        subsets = []
        self.dfs(nums, 0, [False] * len(nums), [], subsets)
        return subsets
    
    def dfs(self, nums, index, visited, subset, subsets):
        subsets.append(list(subset))

        for i in range(index, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == False:
                continue
            subset.append(nums[i])
            visited[i] = True
            self.dfs(nums, i + 1, visited, subset, subsets)
            visited[i] = False
            subset.pop()
