class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * (n + 1)

        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1]

        res = []
        for i, val in enumerate(nums):
            small = i
            large = n - small - 1
            small_res = small * val - pre[small]
            large_res = pre[n] - pre[n - large] - large * val
            res.append(small_res + large_res)
        
        return res