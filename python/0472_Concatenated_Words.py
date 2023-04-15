class Solution:
    def findAllConcatenatedWordsInADict(self, words_list: List[str]) -> List[str]:
        words = set(words_list)
        ans = []

        def canConcatenate(word): # DFS
            if len(word) == 0:
                return True
            for i in range(0, len(word)):
                if word[:i + 1] in words:
                    if canConcatenate(word[i + 1:]):
                        return True
            return False

        for word in words:
            words.remove(word)
            if canConcatenate(word):
                ans.append(word)
            words.add(word)
        
        return ans