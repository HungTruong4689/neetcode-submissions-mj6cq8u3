class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0, x
        while l<=r:
            mid = (l + r) //2
            mul = mid * mid
            if mul == x:
                return mid
            if mul > x:
                r = mid -1
            if mul < x:
                l = mid +1
        return l -1