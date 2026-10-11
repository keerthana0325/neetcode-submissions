class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res = 0
        for i in range(len(s)):
            if s[i] in t:
                a = t.index(s[i])
                if a>=res:
                    res = a
                    t =  t[res+1:]
                    res = 0
            elif s[i] not in t:
                    return False
        return True
