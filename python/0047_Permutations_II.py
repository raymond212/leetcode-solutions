class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        nums.sort()
        permutations = []
        self.dfs(nums, [], permutations, [False] * len(nums))
        return permutations

    def dfs(self, nums, permutation, permutations, visited):
        if len(permutation) == len(nums):
            permutations.append(list(permutation))
            return
    
        for i in range(len(nums)):
            if visited[i] or (i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == False):
                continue
            
            visited[i] = True
            permutation.append(nums[i])
            self.dfs(nums, permutation, permutations, visited)
            permutation.pop()
            visited[i] = False