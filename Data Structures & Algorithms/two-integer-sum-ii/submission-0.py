class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(numbers)):
            if numbers[i] in dic:
                return [dic[numbers[i]],numbers[i]]
            else:
                key = target - numbers[i]
                dic[key] = numbers[i]
        return []