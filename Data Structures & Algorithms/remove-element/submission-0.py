class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        value = 0
        for i in range(len(nums)):
            if nums[i]==val:
                pass
            else:
                temp = nums[value]
                nums[value] = nums[i]
                nums[i] = temp
                value = value+1
        return value
                