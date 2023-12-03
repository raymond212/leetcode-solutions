class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = Counter(chars)
        ans = 0

        for word in words:
            curFreq = Counter(word)
            for c in curFreq:
                if c not in freq or freq[c] < curFreq[c]:
                    break
            else:
                ans += len(word)

        return ans