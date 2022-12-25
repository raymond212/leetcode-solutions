from collections import defaultdict

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Reverse problem: find length of longest substring where count of each letter in the substring is <= total # of that character - k  
        ta = s.count('a') - k
        tb = s.count('b') - k
        tc = s.count('c') - k

        if any(x < 0 for x in [ta, tb, tc]): 
            return -1
        
        freq = {x: 0 for x in "abc"}
        length = 0
        res = 0
        start = 0 # first index of sliding window

        for c in s:
            freq[c] += 1
            length += 1

            while freq['a'] > ta or freq['b'] > tb or freq['c'] > tc:
                freq[s[start]] -= 1
                length -= 1
                start += 1
            
            res = max(res, length)
        
        return len(s) - res
