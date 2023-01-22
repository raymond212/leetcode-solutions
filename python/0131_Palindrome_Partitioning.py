class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        partition = []

        def isPalindrome(a):
            for i in range(len(a) // 2):
                if a[i] != a[len(a) - i - 1]:
                    return False
            return True
        
        def dfs(start, index, s):
            substr = s[start: index + 1]
            if index == len(s) - 1:
                if isPalindrome(substr):
                    partition.append(substr)
                    ans.append(list(partition))
                    partition.pop()
                return
            if isPalindrome(substr):
                partition.append(substr)
                dfs(index + 1, index + 1, s)
                partition.pop()
            dfs(start, index + 1, s)
        
        dfs(0, 0, s)
        return ans