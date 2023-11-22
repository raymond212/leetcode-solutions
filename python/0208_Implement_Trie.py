class Trie:

    def __init__(self):
        self.children = {}
        self.isWord = False

    def insert(self, word: str) -> None:
        for c in word:
            if c not in self.children:
                self.children[c] = Trie()
            self = self.children[c]
        self.isWord = True

    def search(self, word: str) -> bool:
        for c in word:
            if c not in self.children:
                return False
            self = self.children[c]
        return self.isWord

    def startsWith(self, prefix: str) -> bool:
        for c in prefix:
            if c not in self.children:
                return False
            self = self.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)