class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pos = 0
        l= 0
        k = len(flowerbed)
        while l < k:
            if k == 1:
                if flowerbed[l] == 0:
                    pos +=1
            else:
                if l ==0 and flowerbed[0] == 0 and flowerbed[1] == 0:
                    pos +=1
                    flowerbed[0]=1
                elif l == k -1 and flowerbed[-1] == 0 and flowerbed[-2] == 0:
                    pos +=1
                    flowerbed[-1]=1
                else:
                    if l <k-1:
                        if flowerbed[l-1] == 0 and flowerbed[l+1] == 0 and flowerbed[l] == 0:
                            pos +=1
                            flowerbed[l] = 1
            l+=1
                    
        return pos >= n