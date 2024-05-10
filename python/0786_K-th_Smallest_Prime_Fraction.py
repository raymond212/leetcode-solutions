# Binary search solution
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0, 1
        res = []

        while left < right:
            mid = (left + right) / 2
            max_frac = 0
            cnt = 0  # number of smaller fractions
            num, den = 0, 0
            j = 1

            for i in range(n - 1):
                while j < n and arr[i] / arr[j] >= mid:
                    j += 1
                cnt += (n - j)
                if j == n: 
                    break
                fraction = arr[i] / arr[j]
                if fraction > max_frac:
                    num, den, max_frac = i, j, fraction
            
            if cnt == k:
                res = [arr[num], arr[den]]
                break
            elif cnt > k:
                right = mid
            else:
                left = mid

        return res

# Heap solution
class Solution2:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        pq = [(arr[i] / arr[-1], i, n - 1) for i in range(n)]

        for _ in range(k - 1):
            val, num, den = heapq.heappop(pq)
            if den - 1 > num:
                heapq.heappush(pq, (arr[num] / arr[den - 1], num, den - 1))
        
        res = heapq.heappop(pq)
        return [arr[res[1]], arr[res[2]]]
        