# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = {root.val: []}
        self.createGraph(root, graph)
        if len(graph) == 1:
            return 0
        print(graph)
        queue = collections.deque([start])
        visited = {start}
        minutes = 0
        while queue:
            print(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            minutes += 1
        return minutes - 1
                
        
        
    def createGraph(self, node, graph):
        if not node:
            return
        if node.left:
            graph[node.val].append(node.left.val)
            graph[node.left.val] = [node.val]
            self.createGraph(node.left, graph)
        if node.right:
            graph[node.val].append(node.right.val)
            graph[node.right.val] = [node.val]
            self.createGraph(node.right, graph)