class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = nums[0], nums[1]
        if a < b:
            a, b = b, a

        for i in range(2, len(nums)):
            x = nums[i]
            if x > a:
                b = a
                a = x
            elif x > b:
                b = x
        
        return (a - 1) * (b - 1)
