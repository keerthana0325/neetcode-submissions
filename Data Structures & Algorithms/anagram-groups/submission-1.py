class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        # l = []
        ans = []
        for i in range(len(strs)):
            sorted_text = "".join(sorted(strs[i]))
            if sorted_text not in res:
                res[sorted_text] = []
            res[sorted_text].append(strs[i])
                # if len(l) != 0:
                #     ans.append(l)
                # l.clear()
                # l.append(strs[i])
            # elif sorted_text in res:
            #     l.append(strs[i])
        # for k,v in res.items():
        #     ans.append(v)
        return list(res.values())

            
            
        