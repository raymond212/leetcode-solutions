class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        num_rows = 0
        num_cols = 0
        seen_rows = [False] * n
        seen_cols = [False] * n
        ans = 0
        for i in range(len(queries) - 1, -1, -1):
            t, idx, val = queries[i]
            if t == 0:
                if seen_rows[idx]:
                    continue
                ans += val * (n - num_cols)
                seen_rows[idx] = True
                num_rows += 1
            else:
                if seen_cols[idx]:
                    continue
                ans += val * (n - num_rows)
                seen_cols[idx] = True
                num_cols += 1
        return ans
            