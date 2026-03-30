class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        last = ""
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            else:
                if stack:
                    last = stack[-1]
                if last == '(' and i == ')':
                    if stack:
                        stack.pop()
                if last == '[' and i ==']':
                    if stack:
                        stack.pop()
                if last == '{' and i == '}':
                    if stack:
                        stack.pop()

        print(stack)
        return len(stack) == 0