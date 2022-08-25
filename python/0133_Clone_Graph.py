"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        queue = collections.deque([node])
        mapping = {}
        while queue:
            cur_node = queue.popleft()
            if cur_node not in mapping: # if new node
                mapping[cur_node] = Node(cur_node.val)
            for neighbor in cur_node.neighbors:
                if neighbor in mapping: # if neighbor already has been visited
                    mapping[cur_node].neighbors.append(mapping[neighbor])
                    continue
                # if neighbor has not been visited
                mapping[neighbor] = Node(neighbor.val)
                mapping[cur_node].neighbors.append(mapping[neighbor])
                queue.append(neighbor)
        return mapping[node]