class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left, right = 0, 0
        appeared = {}
        res = 0
        
        while right < n:
            if s[right] not in appeared:
                appeared[s[right]] = False
                
            if not appeared[s[right]]:
                appeared[s[right]] = True
                right += 1
            else:
                while left < right:
                    if s[left] == s[right]:
                        left += 1
                        right += 1
                        break               
                    appeared[s[left]] = False
                    left += 1
                    
            res = max(res, right - left)
        
        return res
