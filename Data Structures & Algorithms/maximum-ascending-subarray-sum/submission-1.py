class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = []
        sum1 = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                sum1 += nums[i]
            else:
                res.append(sum1)
                sum1 =nums[i]
        res.append(sum1)
        return max(res)
        