class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pos = 0
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1]==0:   
                pos +=1
            elif i == len(flowerbed) -1 and flowerbed[i] == 0 and flowerbed[i-1]==0:
                pos +=1
            else:

                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    pos +=1
        print(pos)
        return pos == n