class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = 101

        for i in range(n):
            if words[i] == target:
                dist = abs(i - startIndex)
                ans = min(ans, dist, n - dist)
        
        return ans if ans < 101 else -1