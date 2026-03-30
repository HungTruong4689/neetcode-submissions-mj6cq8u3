class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pos = 0
        if len(flowerbed)>1 and flowerbed[0] == 0 and flowerbed[1]==0:   
                pos +=1
        if len(flowerbed)>1 and flowerbed[-1] == 0 and flowerbed[-2]==0:
            pos +=1
        
        for i in range(1,len(flowerbed)-1):
            

                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    pos +=1
        print(pos)
        return pos == n