from heapq import heappush, heappop

class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        total = sum(max(0, num) for num in nums)
        pos = sorted([abs(num) for num in nums])
        s, heap = 0, [(pos[0], 0)]
        for j in range(k - 1):
            s, i = heappop(heap)
            if i + 1 < len(nums):
                heappush(heap, (s - pos[i] + pos[i + 1], i + 1))
                heappush(heap, (s + pos[i + 1], i + 1))
        return total - s