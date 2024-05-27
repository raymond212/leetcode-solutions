class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if nums[0] >= n: 
            return n
        for i in range(1, n):
            x = n - i
            if nums[i - 1] < x <= nums[i]: 
                return x
        return -1