class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j=0,0
        if m >0:
            while i<len(nums1):
                
                if j >=n:
                    break
                
                
                if nums1[i] < nums2[j]:
                    if nums1[i]==0:
                        print("print that line")
                        nums1.insert(i,nums2[j])
                        nums1.pop()
                        j+=1
                    else:
                        i+=1
                else:
                    nums1.insert(i,nums2[j])
                    nums1.pop()
                    j+=1
                print(nums1,i,j,nums1[i])
                
        else:
            nums1[:] = nums2
        print(nums1)
        
        