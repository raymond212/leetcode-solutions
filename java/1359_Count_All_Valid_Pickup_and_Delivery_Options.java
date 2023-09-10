class Solution {
    int MOD = 1000000007;
    public int countOrders(int n) {
        long ans = 1;
        for (int i = 2; i <= n; i++) {
            ans = ans * i * (2 * i - 1) % MOD;
        }
        return (int) ans;
    }
}