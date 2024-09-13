class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            for c in word:
                if c not in allowed:
                    break
            else:
                ans += 1
        return ans