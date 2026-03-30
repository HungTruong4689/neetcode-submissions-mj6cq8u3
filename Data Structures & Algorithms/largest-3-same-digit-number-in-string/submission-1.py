class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res =""

        for i in range(len(num)-3):
            if num[i] == num[i+1]== num[i+2]:
                cand = num[i] + num[i+1] + num[i+2]
                if cand >res:
                    res = cand
        return res