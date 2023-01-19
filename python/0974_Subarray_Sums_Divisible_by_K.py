class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod_freq = defaultdict(int)
        cur_prefix_sum = 0
        mod_freq[0] = 1
        ans = 0
        for i in range(n):
            cur_prefix_sum += nums[i]
            if cur_prefix_sum % k in mod_freq:
                ans += mod_freq[cur_prefix_sum % k]
            mod_freq[cur_prefix_sum % k] += 1
        return ans