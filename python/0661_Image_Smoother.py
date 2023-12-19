class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                total = img[r][c]
                cnt = 1

                for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1], [1, -1], [-1, 1], [1, 1], [-1, -1]]:
                    r_, c_ = r + dr, c + dc
                    if r_ < 0 or r_ >= m or c_ < 0 or c_ >= n:
                        continue
                    total += img[r_][c_]
                    cnt += 1
                
                res[r][c] = total // cnt
        
        return res
