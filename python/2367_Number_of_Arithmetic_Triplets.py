class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        if nums is None or len(nums) < 3:
            return 0
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[k] - nums[j] == diff and nums[j] - nums[i] == diff:
                        count += 1
        return count
            