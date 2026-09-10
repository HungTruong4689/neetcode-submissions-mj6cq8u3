class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i,j =0,0
        m, n = len(word), len(abbr)
        while i < m  and j <n :
            if abbr[j] == '0':
                return False
            if word[i] != abbr[j]:
                sub = ""
                while j<n and abbr[j].isdigit() :
                    sub +=abbr[j]
                    
                    j+=1
                i += int(sub) if sub else 0
            print(i,j)
            
            if j == n:
                continue
            j+=1
            if i == m:
                continue
            i+=1
        
        print(i,j,m,n)


        return i ==m and j ==n