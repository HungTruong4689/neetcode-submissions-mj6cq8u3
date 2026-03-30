class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]* len(temperatures)
        stack = []
        
        for i in range(len(temperatures)-1,-1,-1):
            if i  == len(temperatures)-1:
                stack.append(i)
                res[i] = 0
            if stack:
                j = stack[-1]
                while stack and temperatures[i]> temperatures[stack[-1]]:
                    stack.pop()
                res[i] = stack[-1] -i if stack else 0
                stack.append(i)

        return res