class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a1 = version1.split('.')
        a2 = version2.split('.')
        n = max(len(a1), len(a2))
        
        for i in range(n):
            v1 = 0 if i >= len(a1) else int(a1[i])
            v2 = 0 if i >= len(a2) else int(a2[i])
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        
        return 0