class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        self.dfs(0, len(graph) - 1, graph, [0], paths)
        return paths

    def dfs(self, node, target, graph, path, paths):
        if node == target:
            paths.append(list(path))
            return
        for next_node in graph[node]:
            path.append(next_node)
            self.dfs(next_node, target, graph, path, paths)
            path.pop()
