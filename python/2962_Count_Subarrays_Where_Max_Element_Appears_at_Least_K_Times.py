class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        res = cur = i = 0
        for j in range(len(nums)):
            cur += nums[j] == target
            while cur >= k:
                cur -= nums[i] == target
                i += 1
            res += i
        return res