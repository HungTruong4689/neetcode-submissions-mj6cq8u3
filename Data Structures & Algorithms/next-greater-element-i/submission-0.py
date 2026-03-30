class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for i in range(len(nums2)):
            if i == len(nums2) -1:
                dic[nums2[i]] = -1
            else:
                if nums2[i+1] > nums2[i]:
                    dic[nums2[i]] = nums2[i+1]
                else:
                    dic[nums2[i]] = -1
        result = []
        for i in nums1:
            result.append(dic[i])
        return result