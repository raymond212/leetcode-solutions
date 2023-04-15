class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # find first index >= nums with binary search
        
        left, right = 0, len(nums)
        while (left + 1 < right):
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        
        res = 0
        if nums[left] >= target:
            res = left
        else:
            res = right
        
        return res