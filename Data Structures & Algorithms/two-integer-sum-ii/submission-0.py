class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l = 0
        r = len(numbers)-1
        for i in range(len(numbers)):
            if numbers[l] + numbers[r] == target:
                l = l+1
                r = r+1
                res.extend([l,r])
                break
            elif numbers[l] + numbers[r] > target:
                r =  r-1
            else:
                l = l + 1
        return res
        