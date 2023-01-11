class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(parent, node):
            time = 0
            for child in graph[node]:
                if child == parent:
                    continue
                time += dfs(node, child)
            if node != 0 and (time > 0 or hasApple[node]):
                time += 2
            return time

        return dfs(-1, 0)