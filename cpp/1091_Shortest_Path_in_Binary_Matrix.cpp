#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();

        if (grid[0][0] || grid[n - 1][n - 1]) {
            return -1;
        }

        int dr[8] = {1, 1, -1, -1, 1, 0, -1, 0};
        int dc[8] = {1, -1, 1, -1, 0, 1, 0, -1};

        queue<pair<int, int>> q;
        q.push({0,0});

        int steps = 1;

        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int r = q.front().first;
                int c = q.front().second;
                q.pop();
                if (r == n - 1 && c == n - 1) {
                    return steps;
                }
                for (int j = 0; j < 8; j++) {
                    int nr = r + dr[j];
                    int nc = c + dc[j];
                    if (nr < 0 || nr >= n || nc < 0 || nc >= n || grid[nr][nc] == 1) {
                        continue;
                    }
                    q.push({nr, nc});
                    grid[nr][nc] = 1;
                }
            }
            steps++;
        }
        return -1;
    }
};