class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        return self.binary_search(nums, 0, len(nums) - 1, target)

    def binary_search(self, nums, start, end, target):
        if start > end:
            return -1

        mid = (start + end) // 2
        if nums[mid] > target:
            return self.binary_search(nums, start, mid - 1, target)
        if nums[mid] < target:
            return self.binary_search(nums, mid + 1, end, target)
        return mid