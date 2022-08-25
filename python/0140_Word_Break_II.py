class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> List[str]:
        if not s or not word_dict:
            return []
        lower_dict = set()
        max_length = 0
        for word in word_dict:
            max_length = max(max_length, len(word))
            lower_dict.add(word.lower())
        s = s.lower()
        result = []
        _ = self.dfs(s, 0, [], max_length, result, lower_dict, {})
        return result

    def dfs(self, s, index, words, max_length, result, word_dict, memo):
        if index == len(s):
            sentence = words[0]
            for i in range(1, len(words)):
                sentence = sentence + " " + words[i]
            result.append(sentence)
            return True
        
        if index in memo and memo[index] == False:
            return False

        found = False
        for i in range(index, len(s)):
            if (i + 1 - index) > max_length:
                break
            word = s[index: i + 1]
            if word in word_dict:
                words.append(word)
                res = self.dfs(s, i + 1, words, max_length, result, word_dict, memo)
                if res:
                    found = True
                words.pop()
        
        memo[index] = found
        return found
        