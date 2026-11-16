class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
     
        count = 0
        for i in range(len(flowerbed)):
            if (flowerbed[i] == 0
                and (i == 0 or flowerbed[i-1] == 0)
                and (i == len(flowerbed)-1 or flowerbed[i+1] == 0)):

                flowerbed[i] = 1
                count += 1

        return count >= n
        # count = 0
        # if len(flowerbed)>=3:
        #     for i in range(0, len(flowerbed)-1):
        #         if i == 0:
        #             if flowerbed[i]==0 and flowerbed[i+1]==0:
        #                 count += 1
        #                 flowerbed[i] = 1

        #         elif flowerbed[i] != 0:
        #             continue
        #         elif flowerbed[i-1]==0 and flowerbed[i+1]==0:
        #             count += 1
        #             flowerbed[i] = 1
        # elif len(flowerbed)==1:
        #     if flowerbed[0]==0:
        #         count += 1
        # elif len(flowerbed) == 2:
        #     if flowerbed[0] ==0 and flowerbed[1] == 0:
        #         count += 1

        # return count >= n
         