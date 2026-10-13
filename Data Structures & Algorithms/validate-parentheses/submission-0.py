class Solution:
    def isValid(self, s: str) -> bool:
        p = []
        count = 0
        if s[0]=="}" or s[0] ==")" or s[0]=="]" or s[0]=="":
                return False
        for i in range(len(s)):
            if s[i]=="{" or s[i] =="(" or s[i]=="[":
                p.append(s[i])
                count +=1
            elif s[i] =="}":
                if len(p)==0:
                    return False
                if p[-1] == "{":
                    p.pop()
                    count -=1
                else:
                    return False
            elif s[i] ==")":
                if len(p)==0:
                    return False
                if p[-1] == "(":
                    p.pop()
                    count -=1
                else:
                    return False
            elif s[i] =="]":
                if len(p)==0:
                    return False
                if p[-1]=="[":
                    p.pop()
                    count -=1
                else:
                    return False
        return count==0
            
                
        