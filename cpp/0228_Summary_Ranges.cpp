#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        int n = nums.size();
        vector<string> ans;

        for (int i = 0; i < n; i++) {
            int cur = nums[i];
            while (i + 1 < n && nums[i] + 1 == nums[i + 1]) {
                i++;
            }

            if (nums[i] != cur) {
                ans.push_back(to_string(cur) + "->" + to_string(nums[i]));
            } else {
                ans.push_back(to_string(cur));
            }
        }

        return ans;
    }
};