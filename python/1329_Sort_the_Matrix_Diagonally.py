from heapq import heappush, heappop
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        startingPoints = [(i, 0) for i in range(n)]
        for j in range(1, m):
            startingPoints.append((0, j))
        print(startingPoints)
        for x, y in startingPoints:
            i, j = x, y
            pq = []
            while i < n and j < m:
                heappush(pq, mat[i][j])
                i += 1
                j += 1
            i, j = x, y
            while i < n and j < m:
                mat[i][j] = heappop(pq)
                i += 1
                j += 1
        return mat