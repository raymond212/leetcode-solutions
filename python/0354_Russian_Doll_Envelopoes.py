class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1])) # sort first by ascending, second by descending. Guarantees earlier envelopes will fit

        n = len(envelopes)
        lis = [float('inf')] * (n + 1)
        lis[0] = -float('inf')

        longest = 0
        for _, h in envelopes:
            index = self.first_gte(lis, h)
            lis[index] = h
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