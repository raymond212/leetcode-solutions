class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        freq = dict(Counter(words))
        n = len(s)
        k = len(words)
        m = len(words[0])
        res = []
        for start in range(m):
            cur_freq = {key : 0 for key in freq}
            if start + k * m > n:
                continue
            for i in range(start, start + k * m, m):
                word = s[i:i+m]
                if word in cur_freq:
                    cur_freq[word] += 1
            if cur_freq == freq:
                res.append(start)
            i = start + m
            while i + k * m <= n:
                old_word = s[i-m:i]
                new_word = s[i+(k-1)*m:i+k*m]
                if old_word in cur_freq:
                    cur_freq[old_word] -= 1
                if new_word in cur_freq:
                    cur_freq[new_word] += 1
                if cur_freq == freq:
                    res.append(i)
                i += m
        return res

            
