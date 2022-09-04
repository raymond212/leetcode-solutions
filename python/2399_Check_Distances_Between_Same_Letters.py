class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        seen = [False] * 26
        for i in range(len(s)):
            if seen[ord(s[i]) - ord('a')]:
                continue
            for j in range(i + 1, len(s)):
                if s[j] == s[i]:
                    if distance[ord(s[i]) - ord('a')] == j - i - 1:
                        seen[ord(s[i]) - ord('a')] = True
                    else:
                        return False
        return True