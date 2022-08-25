class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1

        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[len(nums) - 1]:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while right >= left:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[0]:  # if the left part is ordered
                left = mid + 1
            else:
                right = mid - 1
