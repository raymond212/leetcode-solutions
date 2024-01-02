#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string helper(string &s, int l, int r) {
        while (l >= 0 && r < s.size() && s[l] == s[r]) {
            l--;
            r++;
        }
        return s.substr(l + 1, r - l - 1);
    }
    string longestPalindrome(string s) {
        string res = "";

        for (int i = 0; i < s.size(); i++) {
            string cur = helper(s, i, i);
            if (cur.size() > res.size()) {
                res = cur;
            }
            cur = helper(s, i, i + 1);
            if (cur.size() > res.size()) {
                res = cur;
            }
        }

        return res;
    }
};