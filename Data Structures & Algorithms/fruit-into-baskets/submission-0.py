class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        s = set()
        l = 0
        for r in range(len(fruits)):
            s.add(fruits[r])
            while len(s)>2:
                s.discard(fruits[l])
                l+=1
            
            res = max(res,r-l+1)
        return res