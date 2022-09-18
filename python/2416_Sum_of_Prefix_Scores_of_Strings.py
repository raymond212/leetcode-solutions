class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        freq = {}
        for word in words:
            for i in range(1, len(word) + 1):
                prefix = word[0: i]
                freq[prefix] = freq.get(prefix, 0) + 1
        res = []
        for word in words:
            score_sum = 0
            for i in range(1, len(word) + 1):
                prefix = word[0: i]
                score_sum += freq[prefix]
            res.append(score_sum)
        return res