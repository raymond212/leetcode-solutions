class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        if not arr:
            return 0
        arr.sort()
        MOD = int(1e9 + 7)
        dp = {x: 1 for x in arr} # dp[x] represents the number of binary trees with x as the root
        for i in range(len(arr)):
            num = arr[i]
            for j in range(i):
                f_1 = arr[j]
                f_2 = num // f_1
                if num % f_1 != 0 or f_2 not in dp:
                    continue
                dp[num] += dp[f_1] * dp[f_2]
        return sum(dp.values()) % MOD
                    
                