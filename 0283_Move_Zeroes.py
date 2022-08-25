class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                if left != right:
                    nums[left] = nums[right]
                left += 1
            right += 1

        while left < len(nums):
            if nums[left] != 0:
                nums[left] = 0
            left += 1
