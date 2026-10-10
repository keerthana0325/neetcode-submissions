class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        r = {}
        for i in s:
            d[i] = d.get(i,0)+1
        for j in t:
            r[j] = r.get(j,0)+1
        return d == r

        