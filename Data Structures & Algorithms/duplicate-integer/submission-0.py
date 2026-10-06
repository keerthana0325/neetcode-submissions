class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d= {}
        for i in nums:
            d[i] = d.get(i,0)+1
        for key, value in d.items():
            if value>1:
                return True
        return False

        