class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        mapping = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i not in mapping:
                stack.append(i)
            if len(stack)>0:
                top = stack[-1]
                print(top)
                if top == mapping.get(i):
                    stack.pop()
        return len(stack) == 0