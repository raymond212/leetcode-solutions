class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        if not nums:
            return -1

        start, end = 0, len(nums)
        # mountain is the first index so that nums[i] > nums[i + 1]
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid

        if nums[start] > nums[end]:
            return start
        return end