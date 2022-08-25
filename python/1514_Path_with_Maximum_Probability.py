from heapq import heappush, heappop

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = self.construct_graph(edges, succProb)
        visited = set()
        
        max_heap = [(-1, start)]
        
        while max_heap:
            prob, node = heappop(max_heap)
            visited.add(node)
            if node == end:
                return -prob
            for neighbor, p in graph.get(node, []):
                if neighbor in visited:
                    continue
                new_prob = -1 * abs(prob * p)
                heappush(max_heap, (new_prob, neighbor))
        
        return 0
        
        
        
        
    def construct_graph(self, edges, probs):
        graph = {}
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            prob = probs[i]
            graph.setdefault(u, []).append((v, prob))
            graph.setdefault(v, []).append((u, prob))
        return graph