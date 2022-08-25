class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        if not arr:
            return 0
        
        n = len(arr)
        mapping = {}
        for i in range(n):
            if arr[i] in mapping:
                mapping[arr[i]].append(i)
            else:
                mapping[arr[i]] = [i]
        
        copy = sorted(list(set(arr)))
        dp = [1] * n
        
        for i in range(len(copy)):
            val = copy[i]
            for index in mapping[val]:
                for j in range(1, d + 1):
                    if index - j >= 0 and arr[index - j] < val:
                        dp[index] = max(dp[index], dp[index - j] + 1)
                    else:
                        break
                for j in range(1, d + 1):
                    if index + j < n and arr[index + j] < val:
                        dp[index] = max(dp[index], dp[index + j] + 1)
                    else:
                        break
        
        return max(dp)