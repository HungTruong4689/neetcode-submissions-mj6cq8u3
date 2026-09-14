class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,k=0,0,0
        if m ==0 and n >0:
            nums1[:] = nums2
        else:
            temp = [0] * (m+n)
            while i <m and j<n:
                if nums1[i] <=nums2[j]:
                    temp[k] = nums1[i]
                    i+=1
                else:
                    temp[k]= nums2[j]
                    j+=1
                k+=1
            print(temp,i,j,k)
            while i<m:
                temp[k]= nums1[i]
                i+=1
                k+=1
            
            while j<n:
                print(k,j,n,temp)
                temp[k]=nums2[j]
                j+=1
                k+=1
            nums1[:] = temp
        print(nums1)
        