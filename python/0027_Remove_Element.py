class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        k = 0
        
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[pointer] = nums[i]
            pointer += 1
            k += 1
        
        return k