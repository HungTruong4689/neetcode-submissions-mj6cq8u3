class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        countDel = 0
        while left <= right:
            print("left, right: " + str(left)+" "+ str(right))
            if s[left] != s[right]:
                print("check condition before "+ str(s[left] == s[right -1]) +","+ str(s[left+1] == s[right]))
                if s[left] == s[right -1]:
                    left +=1
                    right -=2
                    print("countDel "+ str(countDel))
                    if countDel >1:
                        return False
                    countDel +=1
                    print("after condition 1 "+ str(left)+" "+ str(right))
                elif s[left+1] == s[right]:
                    left +=2
                    right -=1
                    if countDel >1:
                        return False
                    countDel +=1

                else:
                    return False
            else:
                left +=1
                right -=1
            
        return True
        