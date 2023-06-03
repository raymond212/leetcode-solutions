#include <vector>
#include <queue>
#include <cstring>

using namespace std;

class Solution {
public:
    int numOfMinutes(int n, int head, vector<int>& manager, vector<int>& informTime) {
        vector<vector<int>> g(n);
        for (int i = 0; i < n; i++) {
            if (i == head) {
                continue;
            }
            g[manager[i]].push_back(i);
        }
        vector<int> t(n, 0);
        queue<int> q;
        q.push(head);
        int ans = 0;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            if (g[u].empty()) {
                ans = max(ans, t[u]);
                continue;
            }
            for (int v : g[u]) {
                q.push(v);
                t[v] = t[u] + informTime[u];
            }
        }
        return ans;
    }
};