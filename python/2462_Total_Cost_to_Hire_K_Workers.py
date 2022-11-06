import bisect

class Solution:
    def totalCost(self, costs, k: int, candidates: int) -> int:
        n = len(costs)
        
        if 2 * candidates >= n: 
            costs.sort()
            return sum(costs[:k])
        
        first = sorted(costs[:candidates])                     
        last = sorted(costs[n - candidates:])
        
        firstAdd = candidates # next element that gets merged into first
        lastAdd = n - candidates - 1 # next element that gets merged into last

        res = 0

        for i in range(k):
            if len(last) == 0 or (len(first) > 0 and first[0] <= last[0]):  # if best candidate is in first part
                res += first[0]
                first.pop(0)
                if firstAdd <= lastAdd:
                    bisect.insort(first, costs[firstAdd])
                    firstAdd += 1
            else:
                res += last[0]
                last.pop(0)
                if firstAdd <= lastAdd:
                    bisect.insort(last, costs[lastAdd])
                    lastAdd -= 1

        return res