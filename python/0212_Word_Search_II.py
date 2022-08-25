DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if board is None or len(board) == 0:
            return []
        
        word_set = set(words)
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])
        
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search(board, i, j, board[i][j], word_set, prefix_set, set([(i, j)]), result)
        
        return list(result)
        
    def search(self, board, x, y, word, word_set, prefix_set, visited, result):
        if word not in prefix_set:
            return
        
        if word in word_set:
            result.add(word)
        
        for delta_x, delta_y in DIRS:
            next_x = x + delta_x
            next_y = y + delta_y
            if not (0 <= next_x < len(board) and 0 <= next_y < len(board[0])):
                continue
            
            if (next_x, next_y) in visited:
                continue
            
            visited.add((next_x, next_y))
            self.search(board, next_x, next_y, word + board[next_x][next_y], word_set, prefix_set, visited, result)
            visited.remove((next_x, next_y))

