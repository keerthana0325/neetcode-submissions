class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(d[11:13]) > 60 for d in details)
        # count = 0
        # for i in range(len(details)):
        #     if int(details[i][11:13])>60:
        #         count +=1
        # return count
            

        