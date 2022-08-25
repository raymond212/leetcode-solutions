class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = None

        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if res is None or abs(sum - target) < abs(res - target):
                    res = sum 
                    
                if sum <= target:
                    left += 1
                else:
                    right -= 1

        return res