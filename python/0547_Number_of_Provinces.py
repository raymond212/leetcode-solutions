class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(u):
            visited[u] = True
            for v in range(n):
                if isConnected[u][v] and not visited[v]:
                    dfs(v)

        ans = 0

        for u in range(n):
            if visited[u]:
                continue
            dfs(u)
            ans += 1
        
        return ans