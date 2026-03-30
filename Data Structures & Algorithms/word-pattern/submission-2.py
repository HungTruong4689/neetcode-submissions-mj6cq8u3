class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        dic = {}
        rev = {}
        if len(pattern) != len(arr):
            return False
        for i in range(len(pattern)):
            if pattern[i] in dic:
                if arr[i] != dic[pattern[i]]:
                    return False
            else:
                dic[pattern[i]] = arr[i]
            if arr[i] in rev:
                if pattern[i] != rev[arr[i]]:
                    return False
            else:
                rev[arr[i]] = pattern[i]
        print(arr,dic)
        return True