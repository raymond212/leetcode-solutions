class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        k = n // 20
        arr.sort()
        tot = 0
        for i in range(k, n - k):
            tot += arr[i]
        return tot / (n - 2 * k)