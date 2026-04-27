class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = h//len(piles)
        m = max(piles)
        return m//n