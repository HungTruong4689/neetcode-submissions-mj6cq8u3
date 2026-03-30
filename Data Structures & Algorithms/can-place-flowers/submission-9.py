class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pos = 0
        l= 0
        f = [0] + flowerbed + [0]
        for i in range(1,len(f)-1):
            if f[i] ==0 and f[i-1] ==0 and f[i+1]==0:
                pos +=1
                f[i] = 1
        
                    
        return pos >= n