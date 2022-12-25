from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        ans = [0] * n
        count = [1] * n

        self.dfs(0, None, graph, ans, count)
        self.dfs2(0, None, graph, ans, count, n)
        return ans

    def dfs(self, node, parent, graph, ans, count):
        for child in graph[node]:
            if child == parent:
                continue
            self.dfs(child, node, graph, ans, count)
            count[node] += count[child]
            ans[node] += ans[child] + count[child]
    
    def dfs2(self, node, parent, graph, ans, count, n):
        for child in graph[node]:
            if child == parent:
                continue
            ans[child] = ans[node] - count[child] + n - count[child]
            self.dfs2(child, node, graph, ans, count, n)

# TLE O(n^2) 
# class Solution:
#     def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
#         g = {i: set() for i in range(n)}
#         for a, b in edges:
#             g[a].add(b)
#             g[b].add(a)
        
#         answer = [0] * n
#         memo = {} # stores the shortest distance between two nodes
#         for i in range(n): # any node could be root, start with 0
#             for target in range(n): # target node
#                 if target == i:
#                     continue
#                 key = (min(i, target), max(i, target))
#                 _, dist = self.findDist(i, target, g, memo, {i})
#                 answer[i] += dist

#         return answer

#     def findDist(self, i, target, g, memo, visited): # finds the shortest distance from i to j
#         if i == target:
#             return True, 0

#         key = (min(i, target), max(i, target))
#         if key in memo:
#             return True, memo[key]
        
#         res = 0
#         for neighbor in g[i]:
#             if neighbor in visited:
#                 continue
#             visited.add(neighbor)
#             path_exists, dist = self.findDist(neighbor, target, g, memo, visited)
#             if path_exists:
#                 res = dist + 1
#                 break
        
#         if res > 0: # valid path
#             memo[key] = res
#             return True, res

#         return False, 0