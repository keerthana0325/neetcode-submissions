class Solution:
     def plusOne(self, digits: List[int]) -> List[int]:
        s = []
        new = "".join(map(str,digits))
        newnumber = str(int(new)+1)
        for i in range(len(newnumber)):
            p = int(newnumber[i])
            s.append(p)    
        return s  