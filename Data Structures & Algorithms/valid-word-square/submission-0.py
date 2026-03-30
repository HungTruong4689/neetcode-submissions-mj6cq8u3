class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        newArr = []
        for i in range(len(words)):
            word = ""
            for j in range(len(words[i])):
                if words[i][j]:
                    word += words[i][j]
            print(word)
            newArr.append(word)
        
        for z in range(len(words)):
            if words[z] != newArr[z]:
                return False
            else:
                return True

        