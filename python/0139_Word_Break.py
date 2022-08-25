class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        if not s:
            return True

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        max_length = max([
            len(word)
            for word in word_dict
        ]) if word_dict else 0

        # function
        for i in range(1, n + 1):
            for l in range(1, max_length + 1):
                if i < l:
                    break
                if not dp[i - l]:
                    continue
                word = s[i - l:i]
                if word in word_dict:
                    dp[i] = True
                    break
        
        return dp[n]