# O(n^2) DP solution
class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n # length of LIS from beginning to dp[i], ending on dp[i]
        
            
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

# O(nlogn) solution
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int: 
        if not nums:
            return 0
        
        lis = [float('inf')] * (len(nums) + 1)
        lis[0] = -float('inf')

        longest = 0
        for num in nums:
            index = self.first_gte(lis, num)
            lis[index] = num
            longest = max(longest, index)

        return longest
    
    def first_gte(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] >= target:
            return start
        return end