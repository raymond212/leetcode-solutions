class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = [set() for _ in range(n)]
        for x, y in edges:
            graph[x - 1].add(y - 1)
            graph[y - 1].add(x - 1)
        
        odd = []
        for i in range(n):
            if len(graph[i]) % 2 == 1:
                odd.append(i)
        
        if len(odd) > 4 or len(odd) == 3 or len(odd) == 1:
            return False
        if len(odd) == 0:
            return True
        if len(odd) == 2:
            a, b = odd[0], odd[1]
            if a not in graph[b]: # If they are not yet connected, we can connect them
                return True
            for i in range(n): # Search for an even node that neither of them are connected to yet
                if i == a or i == b:
                    continue
                if i not in graph[a] and i not in graph[b]:
                    return True
            return False
        if len(odd) == 4: # There must be two pairs of disconnected nodes 
            a, b, c, d = odd[0], odd[1], odd[2], odd[3] 
            if a not in graph[b] and c not in graph[d]:
                return True
            if a not in graph[c] and b not in graph[d]:
                return True
            if a not in graph[d] and b not in graph[c]:
                return True
        return False
        