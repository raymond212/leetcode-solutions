class Solution:
    def numOfWays(self, n: int) -> int:
        A = B = 6
        mod = 10 ** 9 + 7

        for _ in range(1, n):
            A, B = (2 * A + 2 * B) % mod, (2 * A + 3 * B) % mod

        return (A + B) % mod

        # ABC ABA
        # ACB ACA
        # BAC BAB
        # BCA BCB
        # CAB CAC
        # CBA CBC
        # 
        # ABC <- BCA, CAB, BAB, BCB
        # ABA <- BAC, CAB, BAB, BCB, CAC
        #
        # symmetry holds
        # type A = 6 * (type A prev / 6 * 2 + type B prev / 6 * 2)
        # type B = 6 * (type A prev / 6 * 2 + type B prev / 6 * 3)