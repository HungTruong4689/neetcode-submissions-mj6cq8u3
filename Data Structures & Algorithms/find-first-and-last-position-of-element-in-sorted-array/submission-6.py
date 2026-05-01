class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def deepSearch(isLeft):
            l,r = 0, len(nums)-1
            i = -1
            
            while l<=r:
                m = (l+r)//2
                if target >nums[m]:
                    l = m+1
                elif target <nums[m]:
                    r = m-1
                else:
                    i = m
                    if isLeft:
                        r = m-1
                    else:
                        l = m+1
            return i
            
        return [deepSearch(True),deepSearch(False)]