class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        count = l**2 + l
        while l**2 + l <= 2 *n:
            l +=1
        return l -1