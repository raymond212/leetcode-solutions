class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        return self.isLower(word, 1, n) or self.isUpper(word, 0, n)

    def isLower(self, word, start, end):
        return not any([word[i].isupper() for i in range(start, end)])

    def isUpper(self, word, start, end):
        return not any([word[i].islower() for i in range(start, end)])