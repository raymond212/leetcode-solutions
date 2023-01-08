from bisect import bisect_left, bisect_right

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(bisect_left(nums, 0), len(nums) - bisect_right(nums, 0))