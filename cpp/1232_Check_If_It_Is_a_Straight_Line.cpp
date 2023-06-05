#include <vector>

using namespace std;

class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& c) {
        int dx = c[1][0] - c[0][0];
        int dy = c[1][1] - c[0][1];
        for (int i = 2; i < c.size(); i++) {
            int cdx = c[i][0] - c[0][0];
            int cdy = c[i][1] - c[0][1];
            if (cdx * dy != cdy * dx) {
                return false;
            }
        }
        return true;
    }
};