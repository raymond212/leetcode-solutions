#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        int top = 0, bottom = m - 1, left = 0, right = n - 1;
        int d = 1;
        vector<int> ans;

        while (bottom >= top && right >= left) {
            if (d == 1) {
                for (int c = left; c <= right; c++) ans.push_back(matrix[top][c]);
                top++;
            } else if (d == 2) {
                for (int r = top; r <= bottom; r++) ans.push_back(matrix[r][right]);
                right--;
            } else if (d == 3) {
                for (int c = right; c >= left; c--) ans.push_back(matrix[bottom][c]);
                bottom--;
            } else {
                for (int r = bottom; r >= top; r--) ans.push_back(matrix[r][left]);
                left++;
            }
            d = (d + 1) % 4;
        }

        return ans;
    }
};