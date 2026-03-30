class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids[::-1]:
            if not stack:
                stack.append(i)
            else:
                val = stack[-1]
                if val < 0 and i >0:
                    if abs(val)< abs(i):
                        stack.pop()
                        stack.append(i)
                    while stack and stack[-1]<0 and i >0 and abs(stack[-1])<abs(i):
                        stack.pop()
                    
                    #stack.append(i)

                    if stack and abs(val) == abs(i):
                        stack.pop()
                else:
                    stack.append(i)

              
        return stack[::-1]

