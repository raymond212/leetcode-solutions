#include <iostream>

using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.size(), l = needle.size();
        for (int i = 0; i <= n - l; i++) {
            int j = 0;
            while (j < l) {
                if (haystack[i + j] == needle[j]) j++;
                else break;
            }
            if (j == l) return i;
        }
        return -1;
    }
};