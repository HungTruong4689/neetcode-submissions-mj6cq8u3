class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        newArr = []
        length = len(s)
        for i in range(length-1,-1,-1):
            newArr.append(s[i])
        for i in range(length):
            s[i] = newArr[i]
        