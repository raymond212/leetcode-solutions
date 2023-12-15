class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = set([p[0] for p in paths])

        for _, end in paths:
            if end not in start:
                return end
    