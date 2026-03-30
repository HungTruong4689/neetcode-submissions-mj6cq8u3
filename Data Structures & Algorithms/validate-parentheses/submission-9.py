class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        mapping = {")": "(", "}": "{", "]": "["}
        if len(s)%2 != 0:
            return False
        for i in s:
            
            top = stack[-1] if len(stack)>0 else '#'
            print(top)
            if top == mapping.get(i):
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0