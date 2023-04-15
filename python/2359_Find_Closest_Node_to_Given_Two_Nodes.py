class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        dist_1 = {}
        dist_2 = {}

        def bfs(node, dist):
            q = deque([node])
            dist[node] = 0
            steps = 1
            while q:
                size = len(q)
                for _ in range(size):
                    cur = q.popleft()
                    next_node = edges[cur]
                    if next_node == -1 or next_node in dist:
                        continue
                    dist[next_node] = steps
                    q.append(next_node)
                steps += 1
        
        bfs(node1, dist_1)
        bfs(node2, dist_2)

        max_dist, ans = float('inf'), -1

        for node in range(len(edges)):
            if node not in dist_1 or node not in dist_2:
                continue
            cur_dist = max(dist_1[node], dist_2[node])
            if cur_dist < max_dist:
                max_dist = cur_dist
                ans = node
        
        return ans

