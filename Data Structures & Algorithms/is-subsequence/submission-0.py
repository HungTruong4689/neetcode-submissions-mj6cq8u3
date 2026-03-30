class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)> len(t):
            return False
        arr = []
        lastEl = -1
        for i in s:
            index = t.find(i)
            print(i,index)
            
            
            
            if index == -1:
                return False
            if index > lastEl:
                arr.append(index)
            lastEl = index
            
        
        for i in range(1,len(arr)):
            if arr[i-1]> arr[i]:
                return False
        print(arr)
        return True

        