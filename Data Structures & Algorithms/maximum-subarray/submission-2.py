class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        sum1 = 0
        maxi = float('-inf')
        for i in range(len(nums)):
            sum1 += nums[i]
            if sum1>maxi:
                maxi = sum1
            if sum1<0:
                sum1 = 0
        return maxi 
        # if len(nums)==0:
        #     return 0
        # if len(nums)==1:
        #     return nums[0]
        # sum1 = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)+1):
        #         if sum(nums[i:j])>sum1:
        #             sum1 = sum(nums[i:j])
        # return sum1
        