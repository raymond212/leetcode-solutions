import collections

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = {i: set() for i in range(n)}
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        
        q = collections.deque([source])
        visited = {source}

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for neighbor in g[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                q.append(neighbor)
        
        return False