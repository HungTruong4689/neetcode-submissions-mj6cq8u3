class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for i in details:
            age = int(i[-4:-2])
            if age > 60:
                result +=1
        return result