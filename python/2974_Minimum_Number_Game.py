class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res = sorted(nums)
        for i in range(0, len(nums), 2):
            res[i], res[i + 1] = res[i + 1], res[i]
        return res