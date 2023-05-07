#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int>m;
        for (auto c : s) {
            m[c]++;
        }
        int ans = 0;
        bool extra = false;
        for (auto x : m) {
            int val = x.second;
            ans += val - (val % 2);
            if (!extra && val % 2 == 1) {
                ans++;
                extra = true;
            }
        }
        return ans;
    }
};