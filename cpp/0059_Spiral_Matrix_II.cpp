#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        int top = 0, bottom = n - 1, left = 0, right = n - 1;
        int cnt = 1;
        int d = 1;
        vector<vector<int>> ans(n, vector<int> (n, 0));

        while (bottom >= top && right >= left) {
            if (d == 1) {
                for (int c = left; c <= right; c++) ans[top][c] = cnt++;
                top++;
            } else if (d == 2) {
                for (int r = top; r <= bottom; r++) ans[r][right] = cnt++;
                right--;
            } else if (d == 3) {
                for (int c = right; c >= left; c--) ans[bottom][c] = cnt++;
                bottom--;
            } else {
                for (int r = bottom; r >= top; r--) ans[r][left] = cnt++;
                left++;
            }
            d = (d + 1) % 4;
        }

        return ans;
    }
};