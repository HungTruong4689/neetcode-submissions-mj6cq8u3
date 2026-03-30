class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            print("left, right: " + str(left)+" "+ str(right))
            if s[left] != s[right]:
                print("check condition "+ str(s[left] == s[right -1]) +","+ str(s[left+1] == s[right]))
                if s[left] == s[right -1]:
                    left +=1
                    right -=2
                elif s[left+1] == s[right]:
                    left +=2
                    right -=1

                else:
                    return False
            left +=1
            right -=1
        return True
        