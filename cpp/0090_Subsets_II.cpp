#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        vector<int> sub;
        dfs(nums, 0, sub, ans);
        return ans;
    }
    void dfs(vector<int>& nums, int i, vector<int>& sub, vector<vector<int>>& ans) {
        ans.push_back(sub);
        for (int j = i; j < nums.size(); j++) {
            if (j == i || nums[j] != nums[j - 1]) {
                sub.push_back(nums[j]);
                dfs(nums, j + 1, sub, ans);
                sub.pop_back();
            }
        }
    }
};