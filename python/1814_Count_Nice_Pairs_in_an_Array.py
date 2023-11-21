class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        d = defaultdict(int)
        ans = 0

        for i in range(len(nums)):
            x = nums[i] - int(str(nums[i])[::-1])
            ans += d[x]
            d[x] += 1
        
        return ans % int(1e9 + 7)