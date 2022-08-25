class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 2:
            return False
        n = len(nums)
        if n == 2:
            return nums[0] == nums[1]
        # state
        dp = [False] * (n + 1)  # dp[i] represents if the first i integers have a valid partition
        dp[0] = True
        false_count = 0
        if nums[0] == nums[1]:
            dp[2] = True
        else:
            false_count = 2

        for i in range(3, n + 1):
            if false_count == 3:
                break
            j = i - 1
            if dp[i - 2] and nums[j - 1] == nums[j]:
                dp[i] = True
            elif dp[i - 3] and nums[j - 2] == nums[j - 1] == nums[j]:
                dp[i] = True
            elif dp[i - 3] and nums[j - 1] - nums[j - 2] == nums[j] - nums[j - 1] == 1:
                dp[i] = True
            elif j >= 4:
                if nums[j - 4] == nums[j - 3] == nums[j - 2] == nums[j - 1] == nums[j]:
                    dp[i] = True
                elif nums[j - 4] == nums[j - 3] == nums[j - 2] and nums[j - 1] - nums[j - 2] == nums[j] - nums[
                    j - 1] == 1:
                    dp[i] = True
            if not dp[i]:
                false_count += 1
            else:
                false_count = 0
        return dp[n]
    