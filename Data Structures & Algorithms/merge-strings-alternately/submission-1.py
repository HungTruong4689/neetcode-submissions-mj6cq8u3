class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        m,n = len(word1),len(word2)
        merge = ''
        while i < m and j < n:
            merge += word1[i] + word2[j]
            i+=1
            j+=1
        if i < m:
            merge +=word1[i:]
        if j <n:
            merge += word2[j:]
        return merge