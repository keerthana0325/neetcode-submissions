class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s = []
        count = 0
        for i in range(len(nums)):
            if nums[i]==1:
                count += 1
            elif nums[i]==0:
                s.append(count)
                count = 0
        s.append(count)
        return max(s)

        