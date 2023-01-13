class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        def dfs(node): 
            include_node = 1 # length of longest path that ends at node
            exclude_node = 0 # length of longest path that excludes node
            max1 = max2 = 0
            for child in children[node]:
                include_child, through_child, exclude_child = dfs(child)
                exclude_node = max(exclude_node, include_child, through_child, exclude_child)
                if s[child] != s[node]:
                    include_node = max(include_node, include_child + 1)
                    if include_child > max1:
                        max2 = max1
                        max1 = include_child
                    elif include_child > max2:
                        max2 = include_child
            through_node = 1 + max1 + max2 # length of longest path that goes through node
            return include_node, through_node, exclude_node 

        return max(dfs(0))
