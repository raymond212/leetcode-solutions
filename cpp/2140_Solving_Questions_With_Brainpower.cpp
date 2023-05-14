#include <iostream>
#include <vector>

using namespace std;

class Solution1 {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        int n = questions.size();
        vector<long long> dp(n, 0);
        dp[n - 1] = questions[n - 1][0];

        for (int i = n - 2; i >= 0; i--) {
            dp[i] = questions[i][0];
            int skip = questions[i][1];
            if (i + skip + 1 < n) {
                dp[i] += dp[i + skip + 1];
            }

            dp[i] = max(dp[i], dp[i + 1]);
        }

        return dp[0];
    }
};

class Solution2 {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        vector<long long> dp(questions.size(), 0);
        return dfs(0, questions, dp);
    }

    long long dfs(int i, vector<vector<int>>& questions, vector<long long>& dp) {
        if (i >= questions.size()) return 0;
        if (dp[i] > 0) return dp[i];

        int points = questions[i][0], skip = questions[i][1];
        return dp[i] = max(dfs(i + 1, questions, dp), points + dfs(i + skip + 1, questions, dp));
    }
};