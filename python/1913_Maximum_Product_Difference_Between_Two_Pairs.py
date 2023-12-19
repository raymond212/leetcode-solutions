class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        d, c, b, a = sorted(nums[:4])

        for i in range(4, len(nums)):
            x = nums[i]
            if x > a:
                a, b = x, a
            elif x > b:
                b = x
            elif x < d:
                c, d = d, x
            elif x < c:
                c = x
        
        return a * b - c * d