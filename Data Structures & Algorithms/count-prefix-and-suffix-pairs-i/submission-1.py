class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            n = len(str1)
            return str1 == str2[:n] and str1 == str2[len(str2)-n:]

        
        l,r = 0,1
        count = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count+=1
        return count