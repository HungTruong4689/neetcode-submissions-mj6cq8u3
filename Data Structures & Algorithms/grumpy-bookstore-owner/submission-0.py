class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        outW = 0
        res = 0
        for i in range(len(grumpy)):
            if grumpy[i] ==0:
                outW += customers[i]
        l,r =0,minutes
        inW = 0
        mW = 0
        for k in range(minutes):
            if grumpy[k] == 0:
                inW += customers[k]
            mW += customers[k]
        res = outW - inW + mW
        print("first line",l,r,outW,inW,mW,outW - inW + mW)
        while r< len(grumpy):
            if grumpy[r] ==0:
                inW += customers[r]
            if grumpy[l] == 0:
                inW -= customers[l]
            mW = mW + customers[r] - customers[l]
            print(l,r,outW,inW,mW,outW - inW + mW)
            res = max(res, outW - inW + mW)
            r+=1
            l+=1
        return res
