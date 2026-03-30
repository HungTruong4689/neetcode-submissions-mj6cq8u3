class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        dic = {}
        for i in range(len(pattern)):
            if pattern[i] in dic:
                if arr[i] != dic[pattern[i]]:
                    return False
            else:
                dic[pattern[i]] = arr[i]
        print(arr,dic)
        return True