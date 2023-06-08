#include <vector>

using namespace std;

class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int l = grid[0].size();
        int j = l - 1;
        int ans = 0;

        for (int i = 0; i < grid.size(); i++) {
            while (j >= 0 && grid[i][j] < 0) {
                j--;
            }
            ans += (l - j - 1);
        } 

        return ans;
    }
};