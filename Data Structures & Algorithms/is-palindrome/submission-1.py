class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(i for i in s if i.isalnum())
        s = s.lower()
        m = 0
        n = len(s)-1
        for j in range(len(s)//2):
            if s[m] == s[n]:
                m = m+1
                n = n-1
            else :
                return False
        return True
            
            
        