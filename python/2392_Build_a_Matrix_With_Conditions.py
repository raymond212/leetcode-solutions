class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        in_degree_v = [0] * (k + 1)
        in_degree_h = [0] * (k + 1)
        edges_v = {i: [] for i in range(1, k + 1)}
        edges_h = {i: [] for i in range(1, k + 1)}
        for above, below in rowConditions:
            in_degree_v[below] += 1
            edges_v[above].append(below)
        for left, right in colConditions:
            in_degree_h[right] += 1
            edges_h[left].append(right)
        
        topo_v = self.topoSort(k, in_degree_v, edges_v)
        topo_h = self.topoSort(k, in_degree_h, edges_h)    
        
        if len(topo_v) != k or len(topo_h) != k:
            return []
        
        res = [[0] * k for _ in range(k)]
        for i in range(k):
            num = topo_v[i]
            for j in range(k):
                if topo_h[j] == num:
                    res[i][j] = num
                    break
        
        return res
    
    def topoSort(self, k, in_degree, edges):
        queue = collections.deque()
        for num in range(1, k + 1):
            if in_degree[num] == 0:
                queue.append(num)
        
        topoOrder = []
        while queue:
            num = queue.popleft()
            topoOrder.append(num)
            for next_num in edges[num]:
                in_degree[next_num] -= 1
                if in_degree[next_num] == 0:
                    queue.append(next_num)
        
        return topoOrder