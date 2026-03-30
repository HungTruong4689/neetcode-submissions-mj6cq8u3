class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(abbr) > len(word):
            return False
        if word == abbr:
            return True
        newStr = ''
        left = 0
        num = ''
        pos = ''
        while left <len(abbr):
            if word[left] != abbr[left]:
                if abbr[left].isdigit():
                    num += abbr[left]
                    pos += str(left)
                else:
                    num == ''
                    pos == ''
            if len(num)>0:
                if num[0] == 0:
                    return False
                checkPos = int(pos[0])
                newPos = int(num)
                print("check Pos "+ str(checkPos)+ " "+ str(newPos))
                newStr = word[:checkPos]+num +word[checkPos+newPos:]
                print("check new string condition: "+ newStr)
            left+=1

        print("check condition: "+newStr+" "+abbr)
        if newStr == abbr:
            return True


        return False