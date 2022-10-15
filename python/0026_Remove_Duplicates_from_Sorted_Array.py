class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numUnique = 1
        lastUnique = 0
        
        for i in range(1, len(nums)):
            if (nums[i] == nums[i - 1]):
                continue
            numUnique += 1
            lastUnique += 1
            nums[lastUnique] = nums[i]
        
        return numUnique
        
        