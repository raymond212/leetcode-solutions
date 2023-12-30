class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = Counter(''.join(words))
        n = len(words)

        return all([val % n == 0 for val in freq.values()])