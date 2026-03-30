class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ""
        m = ""
        for i in s:
            print(m)
            if i not in m:
                m +=i
            else:
                if len(m)>= len(res):
                    res = m
                m = ""
            print(m)
            if len(m)>= len(res):
                    res = m
        return len(res)
            