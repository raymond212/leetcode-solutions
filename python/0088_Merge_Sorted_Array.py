class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        if not A:
            return B
        if not B:
            return A

        i, j, index = m - 1, n - 1, m + n - 1

        while j >= 0:
            if i < 0 or A[i] <= B[j]:
                A[index] = B[j]
                j -= 1
            else:
                A[index] = A[i]
                i -= 1       
            index -= 1
