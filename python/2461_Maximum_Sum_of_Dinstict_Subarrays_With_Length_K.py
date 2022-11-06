class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = [0] * 100001
        
        sum = 0
        res = 0
        watch = set() # duplicated elements
        
        for i, num in enumerate(nums):
            freq[num] += 1
            sum += num
            if freq[num] > 1:
                watch.add(num)
            
            if i < k - 1: # not subarray of sufficient length yet
                continue
                
            if i > k - 1: 
                sum -= nums[i - k]
                freq[nums[i - k]] -= 1
                if nums[i - k] in watch and freq[nums[i - k]] <= 1:
                    watch.remove(nums[i - k])
            
            if len(watch) == 0:
                res = max(res, sum)
        
        return res
            