class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        scores = [0] * n
        for i in range(n):
            scores[edges[i]] += i
        
        max_val = 0
        max_i = 0
        for i in range(n):
            if scores[i] > max_val:
                max_val = scores[i]
                max_i = i
        
        return max_i