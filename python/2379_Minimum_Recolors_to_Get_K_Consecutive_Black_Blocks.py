class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = float('inf')
        for i in range(len(blocks) - k + 1):
            count = 0
            for j in range(i, i + k):
                if blocks[j] == 'W':
                    count += 1
            res = min(res, count)
        return res
            