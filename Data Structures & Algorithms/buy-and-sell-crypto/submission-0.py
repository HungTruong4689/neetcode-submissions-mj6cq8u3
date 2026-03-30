class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mV = 0
        mP = 0
        for i in range(len(prices)-1,-1,-1):
            mV = max(mV,prices[i])
            mP = max(mP,mV - prices[i])


        return mP