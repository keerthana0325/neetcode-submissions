class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLength = 0
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                l = max(l, d[s[i]] + 1)
                d[s[i]] = i
            maxLength = max(maxLength,(i-l)+1)
        return maxLength
        
            


