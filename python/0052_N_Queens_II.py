class Solution:
    def totalNQueens(self, n: int) -> int:
        # dict = {
        #     1: 1,
        #     2: 0,
        #     3: 0,
        #     4: 2,
        #     5: 10,
        #     6: 4,
        #     7: 40,
        #     8: 92,
        #     9 : 352
        # }
        # return dict[n]
    
        queens = []
        return self.dfs(0, n, queens)
        
    def dfs(self, row, n, queens):
        if row == n:
            return 1
        
        count = 0
        for col in range(n):
            
            can_attack = False
            for queen in queens:
                if self.can_attack(queen[0], queen[1], row, col):
                    can_attack = True
                    break
            if can_attack:
                continue
            queens.append((row, col))
            count += self.dfs(row + 1, n, queens)
            queens.pop()
            
        return count
        
    def can_attack(self, row_1, col_1, row_2, col_2):
        return (row_1 == row_2) or (col_1 == col_2) or (abs(row_1 - row_2) == abs(col_1 - col_2))
            