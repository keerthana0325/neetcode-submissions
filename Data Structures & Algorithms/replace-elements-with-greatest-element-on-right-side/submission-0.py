class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[i] = -1
            else:
                sub = arr[i+1:]
                maxi = max(sub)
                arr[i] = maxi         
        return arr