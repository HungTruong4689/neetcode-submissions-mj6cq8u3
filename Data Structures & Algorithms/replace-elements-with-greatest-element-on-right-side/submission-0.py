class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newArr = []
        for i in range(len(arr)):
            if i == len(arr) -1 :
                newArr.append(-1)
            else:
                newArr.append(max(arr[i+1:]))

        return newArr
        