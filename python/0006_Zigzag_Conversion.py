# Cleaner solution
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows # row[i] is the concatenation of the characters in the ith row
        index = 0 # index of the string
        step = 1 # whether we are moving downwards or upwards in the matrix 

        for c in s:
            rows[index] += c
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return "".join(rows)
    
# First solution
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         n = len(s)
#         if numRows == 1 or numRows > n:
#             return s
#         numCols = (n // (2 * numRows - 2) + 1) * (numRows - 1)
#         grid = [[""] * numCols for _ in range(numRows)]
#         down = True
#         x, y = 0, 0
#         for c in s:
#             grid[x][y] = c
#             if down:
#                 if x < numRows - 1:
#                     x += 1
#                 else:
#                     x -= 1
#                     y += 1
#                     down = False
#             else:
#                 if x > 0:
#                     x -= 1
#                     y += 1
#                 else:
#                     x += 1
#                     down = True
#         res = ""
#         for i in range(numRows):
#             for j in range(numCols):
#                 if grid[i][j] != "":
#                     res += grid[i][j]
#         return res
                    
        