#include <iostream>
#include <vector>

using namespace std;

// Bottom up DP
class Solution {
    const int MOD = 1e9 + 7;
public:
    int countGoodStrings(int low, int high, int num_zeros, int num_ones) {
        vector<int> dp(high + 1, 0);
        dp[0] = 1;

        int ans = 0;
        for (int l = 1; l <= high; l++) {
            if (l >= num_zeros) {
                dp[l] = (dp[l] + dp[l - num_zeros]) % MOD;
            }
            if (l >= num_ones) {
                dp[l] = (dp[l] + dp[l - num_ones]) % MOD;
            }
            if (l >= low) {
                ans = (ans + dp[l]) % MOD;
            }
        }

        return ans;
    }
};

// Top down DP
class Solution2 {
    const int MOD = 1e9 + 7;
public:
    int countGoodStrings(int low, int high, int num_zeros, int num_ones) {
        vector<int> dp(high + 1, -1);
        return dfs(0, low, high, dp, num_zeros, num_ones);
    }
    int dfs(int l, int low, int high, vector<int>& dp, int num_zeros, int num_ones) {
        if (l > high) {
            return 0;
        }
        if (dp[l] != -1) {
            return dp[l];
        }
        int ans = 0;
        if (l >= low) {
            ans = 1;
        }
        ans = (ans + dfs(l + num_zeros, low, high, dp, num_zeros, num_ones)) % MOD;
        ans = (ans + dfs(l + num_ones, low, high, dp, num_zeros, num_ones)) % MOD;
        dp[l] = ans;
        return ans;
    }
};