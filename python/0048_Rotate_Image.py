class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n // 2):
            numToRotate = n - 2 * i - 1
            for j in range(i, i + numToRotate):
                i2, j2 = self.rotatePoint90(i, j, n)
                i3, j3 = self.rotatePoint90(i2, j2, n)
                i4, j4 = self.rotatePoint90(i3, j3, n)

                matrix[i][j], matrix[i2][j2], matrix[i3][j3], matrix[i4][j4] = matrix[i4][j4], matrix[i][j], matrix[i2][j2], matrix[i3][j3]

        return matrix

    def rotatePoint90(self, i, j, n):
        return j, n - i - 1