class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        near = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                dist_sq = (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2
                if bombs[i][2] ** 2 >= dist_sq:
                    near[i].append(j)

        def explode(u, seen):
            for v in near[u]:
                if v not in seen:
                    seen.add(v)
                    explode(v, seen)
        
        ans = 0
        for i in range(n):
            seen = {i}
            explode(i, seen)
            ans = max(ans, len(seen))
        
        return ans