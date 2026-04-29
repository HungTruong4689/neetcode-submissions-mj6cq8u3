class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        speed = max(weights)
        l,r =1,max(weights)
        res = 0
        #(sum(weights)/days)
        # while l <=r:
        #     for i in weights:
        while True:
            total = 0
            for i in weights:
                total += i
                if total>speed:
                    total = i
                    res +=1
                print(res)
                if res <= days:

                    return speed
            speed +=1
        return speed