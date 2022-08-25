class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        visited = [False] * n
        queue = collections.deque([0])
        visited[0] = True
        count = 1
        graph = self.generate_graph(n, edges)
        restricted_set = set(restricted)
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in restricted_set or visited[neighbor]:
                    continue
                visited[neighbor] = True
                count += 1
                queue.append(neighbor)
        return count
            
    def generate_graph(self, n, edges):
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph
        