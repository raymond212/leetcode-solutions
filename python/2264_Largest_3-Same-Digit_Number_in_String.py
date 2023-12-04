class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        s = str(num)
        
        for i in range(len(num) - 2):
            cur = s[i:i + 3]
            if cur[0] == cur[1] == cur[2]:
                if not ans:
                    ans = cur
                elif int(cur[0]) > int(ans[0]):
                    ans = cur

        return ans