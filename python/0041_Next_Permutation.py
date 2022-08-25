class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        
        i = n - 1
        j = 0

        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        
        if i != 0:
            j = n - 1
            while nums[j] <= nums[i - 1]:
                j -= 1
            nums[j], nums[i - 1] = nums[i - 1], nums[j]

        self.swap_list(nums, i, n - 1)
        return nums

    def swap_list(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1