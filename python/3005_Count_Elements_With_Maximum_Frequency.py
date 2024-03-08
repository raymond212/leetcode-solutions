class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        arr = list(Counter(nums).values())
        mx = max(arr)
        return arr.count(mx) * mx