class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = arr[i] ^ pre[i]
        return [pre[r + 1] ^ pre[l] for l, r in queries]