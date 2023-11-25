class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * (n + 1)

        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + nums[i - 1]

        res = []
        for i, val in enumerate(nums):
            small = i
            large = n - small - 1
            small_res = small * val - pref[small]
            large_res = pref[n] - pref[n - large] - large * val
            res.append(small_res + large_res)
        
        return res