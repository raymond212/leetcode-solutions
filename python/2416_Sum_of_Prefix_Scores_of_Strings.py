# Using Trie
class Solution1:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = {}
        for word in words:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = [{}, 0]
                cur[c][1] += 1
                cur = cur[c][0]
        
        res = []
        for word in words:
            score_sum = 0
            cur = trie
            for c in word:
                if c not in cur:
                    break
                nxt, score = cur[c]
                score_sum += score
                cur = nxt
            res.append(score_sum)
        return res
    

# Using prefix frequency dict
class Solution2:
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