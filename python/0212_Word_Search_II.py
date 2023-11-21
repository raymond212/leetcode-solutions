class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def addWord(self, word):
        for c in word:
            if c not in self.children:
                self.children[c] = TrieNode()
            self = self.children[c]
        self.is_word = True

    def hasChild(self, c):
        return c in self.children

    def getChild(self, c):
        return self.children[c]

    def isWord(self):
        return self.is_word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if board is None or len(board) == 0:
            return []

        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        m, n = len(board), len(board[0])
        res = set()
        visited = [[False] * n for _ in range(m)]

        def dfs(r, c, node, word):
            if not (0 <= r < m and 0 <= c < n) or visited[r][c] or not node.hasChild(board[r][c]):
                return

            word += board[r][c]
            node = node.getChild(board[r][c])
            visited[r][c] = True

            if node.isWord():
                res.add(word)

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r + dr, c + dc, node, word)
            
            visited[r][c] = False
            
        for r in range(m):
            for c in range(n):
                dfs(r, c, root, "")
        
        return list(res)