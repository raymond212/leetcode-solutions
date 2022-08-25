class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = 1
        k -= 1
        for i in range(n):
            factorial *= (i + 1)

        permutation = []
        nums = [i for i in range(1, n + 1)]

        for i in range(n):
            factorial //= (n - i)
            index = int(k // factorial)
            permutation.append(str(nums[index]))
            del nums[index]
            k %= factorial
            
        return "".join(permutation)