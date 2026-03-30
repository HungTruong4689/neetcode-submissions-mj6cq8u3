class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        newArr = []
        for i in range(len(words[0])):
            word = ""
            for j in range(len(words)):
                
                if i < len(words[j]):
                    word += words[j][i]
            #print(word)
            newArr.append(word)
        
        for z in range(len(words)):
            if words[z] != newArr[z]:
                return False
        return True

        