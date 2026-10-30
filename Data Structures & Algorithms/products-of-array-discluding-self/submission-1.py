class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        ans = []
        for i in range(n):
            ans.append(left[i] * right[i])

        return ans
        # product = 1
        # ans = []
        # for i in range(len(nums)):
        #     for j in range(0,len(nums)):
        #             if i!=j:
        #                 product  *=nums[j]
        #     ans.append(product) 
        #     product = 1
        # return ans
        