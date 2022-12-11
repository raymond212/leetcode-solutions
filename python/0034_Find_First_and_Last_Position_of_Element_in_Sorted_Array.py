class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return -1, -1
            
        first, last = -1, -1

        n = len(nums)

        # find first
        left, right = 0, n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid

        if nums[left] == target:
            first = left
        elif nums[right] == target:
            first = right
        
        # find last
        left, right = 0, n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid
        
        if nums[right] == target:
            last = right
        elif nums[left] == target:
            last = left
        
        return first, last