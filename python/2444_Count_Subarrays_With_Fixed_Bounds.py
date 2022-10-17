class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        nextStart = 0
        lastMin = -1
        lastMax = -1
        
        for i in range(len(nums)):
            if nums[i] > maxK or nums[i] < minK:
                nextStart = i + 1
            if nums[i] == minK: 
                lastMin = i
            if nums[i] == maxK: 
                lastMax = i
            res += max(0, min(lastMin, lastMax) - nextStart + 1)
        
        return res