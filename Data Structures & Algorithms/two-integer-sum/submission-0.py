class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            key = target - nums[i]
            print(hashMap)
            if nums[i] in hashMap:
                return [hashMap[nums[i]],i]
            else:
                hashMap[key] = i
        return []