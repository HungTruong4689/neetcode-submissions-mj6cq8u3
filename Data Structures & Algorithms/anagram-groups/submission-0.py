from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        result = []
        hashMap = {}
        for check in strs:
            key = "".join(sorted(check))
            #print(key)
            if key in hashMap:
                hashMap[key].append(check)
            else:
                print(check)
                hashMap[key] = [check]
        #print(hashMap)
        for key, value in hashMap.items():
            #print(value)
            result.append(value)
        return result



        