class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        while (left < right):
            cur = nums[right] + nums[left]
            if cur == 0:
                return nums[right]
            elif cur > 0:
                right -= 1
            else:
                left += 1
        return -1