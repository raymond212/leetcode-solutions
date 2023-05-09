#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {        
        sort(nums.begin(), nums.end());
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int cur = nums[l] + nums[r];
            if (cur == target) {
                return {l + 1, r + 1};
            } else if (cur < target) {
                l++;
            } else {
                r--;
            }
        }
        return {};
    }
};