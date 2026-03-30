class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            n = len(str1)
            return str1 == str2[:n] and str1 == str2[len(str2)-n:]

        words = sorted(words)
        l,r = 0,1
        count = 0
        while l < len(words)-1:
            while r < len(words) and len(words[l])< len(words[r]):
                if isPrefixAndSuffix(words[l], words[r]):
                    count +=1
                r+=1
            
            l+=1
            r = l+1
        return count