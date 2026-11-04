class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = set()
        for i in range(len(nums)-2):
            p = -nums[i]
            left = i+1
            right = len(nums)-1
            while left<right:
                if nums[left]+nums[right]==p:
                    l.add((nums[i],nums[left],nums[right]))
                    left +=1
                    right -=1
                elif nums[left]+nums[right]<p:
                    left = left+1
                else:
                    right = right-1
        return [list(x) for x in l]

    
        #     imsum = nums[j]+nums[k]
        #     if imsum+p==0:
        #         l.append([nums[i],nums[j],nums[k]])
        # return l
                

            
        