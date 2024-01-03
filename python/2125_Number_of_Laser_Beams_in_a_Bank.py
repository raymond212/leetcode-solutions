class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = ans = 0

        for row in bank:
            cur = row.count('1')
            if cur:
                ans += prev * cur
                prev = cur
        
        return ans