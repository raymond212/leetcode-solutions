class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0] * n
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(parent, node, freq):
            node_pos = ord(labels[node]) - ord('a')
            before = freq[node_pos]
            for child in graph[node]:
                if child == parent:
                    continue
                dfs(node, child, freq)
            freq[node_pos] += 1
            ans[node] = freq[node_pos] - before
        
        dfs(-1, 0, [0] * 26)
        return ans

