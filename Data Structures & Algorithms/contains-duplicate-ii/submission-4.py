class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        for R in range(len(nums)):
            if nums[R] in window:
                if R - L <= k:
                    return True
                else:
                    window.remove(nums[L])
                    L+=1
            else:
                window.add(nums[R])

        return False
            