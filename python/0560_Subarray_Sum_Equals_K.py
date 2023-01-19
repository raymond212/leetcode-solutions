class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cur_prefix_sum = 0
        freq = defaultdict(int)
        freq[0] = 1
        ans = 0
        for i in range(n):
            cur_prefix_sum += nums[i]
            if cur_prefix_sum - k in freq:
                ans += freq[cur_prefix_sum - k]
            freq[cur_prefix_sum] += 1
        return ans