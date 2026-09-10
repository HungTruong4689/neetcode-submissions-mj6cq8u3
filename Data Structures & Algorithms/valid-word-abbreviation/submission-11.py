class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i,j =0,0
        m, n = len(word), len(abbr)
        while i < m  and j <n :
            if abbr[j] == '0':
                return False
            if word[i]==abbr[j]:
                i+=1
                j+=1 
                print(j)
            elif abbr[j].isalpha():
                return False
            else:
                sub = 0
                while j<n and abbr[j].isdigit() :
                    sub = sub* 10 + int(abbr[j])
                    
                    j+=1
                i += sub
            
        
        print(i,j,m,n)


        return i ==m and j ==n