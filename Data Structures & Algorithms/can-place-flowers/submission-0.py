class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pos = 0
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                pos +=1
        print(pos)
        return pos == n