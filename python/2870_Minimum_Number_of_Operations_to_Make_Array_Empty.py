class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0

        for f in freq.values():
            if f == 1:
                return -1
            if f % 3 == 0:
                ans += f // 3
            elif f % 3 == 1:
                ans += (f - 4) // 3 + 2
            else:
                ans += (f - 2) // 3 + 1
        
        return ans