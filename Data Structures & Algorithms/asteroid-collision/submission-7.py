class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if not stack:
                stack.append(i)
            else:
                last = stack[-1]
                if last <0 and i <0:
                    stack.append(i)
                if last >0 and i >0:
                    stack.append(i)
                if last <0 and i >0:
                    stack.append(i)
                if last >0 and i <0:
                    while stack and abs(stack[-1]) <abs(i):
                        
                        stack.pop()
                        # if not stack:
                        #     stack.append(i)
                    
                    
                        
                    if stack and abs(stack[-1]) ==abs(i):
                        
                        if stack[-1] >0 and i >0:
                            stack.append(i)
                        if stack[-1] <0 and i <0:
                            stack.append(i)
                        if stack[-1] >0 and i <0:
                            stack.pop()
                    if not stack:
                        print(stack)
                        stack.append(i)
                        print(stack)
                
                    
        return stack

