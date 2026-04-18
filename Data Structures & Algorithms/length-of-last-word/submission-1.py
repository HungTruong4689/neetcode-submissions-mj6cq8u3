class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        check_arr = [word for word in arr if word != '']
        newstring = check_arr[-1]
        #print(arr,newstring)
        return len(newstring)
        