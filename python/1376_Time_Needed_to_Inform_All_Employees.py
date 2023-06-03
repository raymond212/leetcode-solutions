class Solution:
    def numOfMinutes(self, n: int, head: int, manager: List[int], informTime: List[int]) -> int:
        g = [[] for _ in range(n)]
        for i in range(n):
            if i == head:
                continue
            g[manager[i]].append(i)
        
        q = deque([(head, 0)])

        ans = 0

        while q:
            u, t = q.popleft()
            if not g[u]:
                ans = max(ans, t)
                continue    
            for v in g[u]:
                q.append((v, t + informTime[u]))
        
        return ans
        
