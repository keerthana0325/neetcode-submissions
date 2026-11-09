class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        l = []
        nums = sorted(nums)
        count = 1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            elif abs(nums[i]-nums[i+1])==1:
                count +=1
            else:
                l.append(count)
                count = 1
        l.append(count)  
        return max(l) 