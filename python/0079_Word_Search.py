class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if not (0 <= r < m and 0 <= c < n) or board[r][c] != word[i]:
                return False
            for dr, dc in dirs:
                cur = board[r][c]
                board[r][c] = ''
                found = dfs(r + dr, c + dc, i + 1)
                board[r][c] = cur
                if found:
                    return True
            return False

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False    