class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s[i] in t:
                a = t.index(s[i])
                t =  t[a+1:]
            elif s[i] not in t:
                    return False
        return True
