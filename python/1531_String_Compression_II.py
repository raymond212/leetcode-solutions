class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        @lru_cache(None)
        def dfs(start, last, last_count, remain):
            if remain < 0:
                return float('inf')
            if start == len(s):
                return 0
            if s[start] == last:
                increase = 1 if last_count in (1, 9, 99) else 0
                return increase + dfs(start + 1, last, last_count + 1, remain)
            else:
                # keep
                res1 = 1 + dfs(start + 1, s[start], 1, remain)
                # delete
                res2 = dfs(start + 1, last, last_count, remain - 1)
                return min(res1, res2)

        return dfs(0, '', 0, k)