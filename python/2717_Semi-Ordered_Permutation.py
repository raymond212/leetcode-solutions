class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        small = nums.index(1)
        large = nums.index(n)
        if small < large:
            return (small) + ((n - 1) - large)
        if small > large:
            return (small) + ((n - 1) - large) - 1