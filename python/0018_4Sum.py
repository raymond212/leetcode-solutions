class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        self.dfs(nums, 0, target, 4, [], res)
        return res

    def dfs(self, nums, startI, target, n, result, results):
        if len(nums) < n or n < 2 or target < nums[startI] * n or target > nums[-1] * n:
            return

        if n == 2:
            l, r = startI, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: # avoid duplicates
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(startI, len(nums) - n + 1):
                if i == startI or (i > startI and nums[i] != nums[i - 1]):  # avoid duplicates
                    result.append(nums[i])
                    self.dfs(nums, i + 1, target - nums[i], n - 1, result, results)
                    result.pop()