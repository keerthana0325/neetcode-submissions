class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        cs = [0]*(n+1)
        cs[1] = 1
        cs[2] = 2
        for i in range(3,n+1):
            cs[i] = cs[i-1]+cs[i-2]
        return cs[n]

        