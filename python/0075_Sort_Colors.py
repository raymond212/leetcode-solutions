class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if not nums:
            return

        left, index, right = 0, 0, len(nums) - 1

        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            elif nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
            else:
                index += 1