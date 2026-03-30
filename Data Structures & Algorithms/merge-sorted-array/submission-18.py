class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,k=0,0,0
        tempArr = nums1[:m]
        print(tempArr)
        while k<len(nums1):
            print("k value: "+str(k))
            if j<n and i<m:
            
                if tempArr[i]>= nums2[j]:
                    nums1[k]= nums2[j]
                    j+=1
                else:
                    nums1[k]=tempArr[i]
                    i+=1
            else:
                print("check value of "+str(i)+" "+str(j)+" ")
                if j>=n:
                    print("k, i value 1: "+str(k)+" " +str(i) +" "+ str(tempArr[i]))
                    if i>=m:
                        break
                    nums1[k] = tempArr[i]
                    i+=1
                    
                if i>=m:
                    if j>=n:
                        break
                    nums1[k] = nums2[j]
                    j+=1
                    
            print(nums1)
            k+=1
        print(nums1)
        