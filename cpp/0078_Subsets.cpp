#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> sub;
        dfs(0, nums, sub, ans);
        return ans;
    }
    void dfs(int i, vector<int>& nums, vector<int>& sub, vector<vector<int>>& ans) {
        ans.push_back(sub);
        for (int j = i; j < nums.size(); j++) {
            sub.push_back(nums[j]);
            dfs(j + 1, nums, sub, ans);
            sub.pop_back();
        }
    }
};