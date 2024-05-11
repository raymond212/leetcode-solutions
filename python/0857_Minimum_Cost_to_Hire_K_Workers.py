class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        ans = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > k:
                qsum += heapq.heappop(heap)
            if len(heap) == k:
                ans = min(ans, qsum * r)
        return ans