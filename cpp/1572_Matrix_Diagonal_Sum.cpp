#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int n = mat.size(), ans = 0;
        for (int c = 0; c < n; c++) {
            ans += mat[c][c];
            int r2 = n - c - 1;
            if (r2 != c) {
                ans += mat[r2][c];
            }
        }
        return ans;
    }
};