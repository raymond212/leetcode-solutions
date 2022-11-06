import heapq

class Solution:
    def totalCost(self, costs, k: int, candidates: int) -> int:
        n = len(costs)
        first = sorted(costs[:candidates])                     
        last = sorted(costs[max(candidates, n - candidates):])
        heapq.heapify(first)
        heapq.heapify(last)
        
        firstAdd = candidates # next element that gets merged into first
        lastAdd = n - candidates - 1 # next element that gets merged into last

        res = 0

        for _ in range(k):
            if not last or first and first[0] <= last[0]:  # if best candidate is in first part
                res += heapq.heappop(first)
                if firstAdd <= lastAdd:
                    heapq.heappush(first, costs[firstAdd])
                    firstAdd += 1
            else:
                res += heapq.heappop(last)
                if firstAdd <= lastAdd:
                    heapq.heappush(last, costs[lastAdd])
                    lastAdd -= 1

        return res