class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if i >0:
                stack.append(i)
            if i <0:
                while stack and stack[-1] < abs(i):
                    stack.pop()
                if stack and stack[-1] == abs(i):
                    stack.pop()
                    print(stack)
                
                    
        return stack

