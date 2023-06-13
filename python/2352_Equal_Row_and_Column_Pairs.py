import collections
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = collections.Counter(tuple(row) for row in grid)
        n = len(grid)
        ans = 0

        for c in range(n):
            col = [grid[r][c] for r in range(n)]
            ans += d[tuple(col)]

        return ans