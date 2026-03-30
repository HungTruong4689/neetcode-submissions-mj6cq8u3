class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for i in tokens:
            if i not in operators:
                # If it's a number, push to stack
                stack.append(int(i))
            else:
                # Pop the last two numbers
                # Note: b is the top element, a is the one below it
                b = stack.pop()
                a = stack.pop()
                
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)
                elif i == '*':
                    stack.append(a * b)
                elif i == '/':
                    # Python // is floor division (rounds toward -inf)
                    # LeetCode usually requires truncation toward zero
                    # Use int(a / b) to truncate toward zero
                    stack.append(int(a / b))
                    
        return stack[0]