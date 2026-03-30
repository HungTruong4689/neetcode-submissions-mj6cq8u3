class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        sVal = 0
        for i in range(k):
            sVal += arr[i]
        aver = sVal //k
        if aver >= threshold:
            count+=1
        l = 0
        for i in range(k,len(arr)):
            sVal = sVal + arr[i] - arr[l]
            aver = sVal //k
            if aver >= threshold:
                count+=1
            l+=1
        return count