class Solution:
    def isPathCrossing(self, path: str) -> bool:
        begin = [0,0]
        check = [[0,0]]
        print(check)
        for i in path:
            if i == "N":
                begin[1] +=1
                
            elif i == "E":
                begin[0] +=1
                
            elif i == "S":
                begin[1] -=1
                
            else:
                begin[0] -=1
            print(check,begin)
            if begin in check:
                return True
                check.append(begin)    
            print(check)
        return False