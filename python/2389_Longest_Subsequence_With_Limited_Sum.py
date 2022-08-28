class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []
        for query in queries:
            sum = 0
            ans = len(nums)
            for i in range(len(nums)):
                sum += nums[i]
                if sum > query:
                    ans = i
                    break
            res.append(ans)
        return res