class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        S = skill[0]+skill[-1]
        res = skill[0]*skill[-1]
        l,r = 1, len(skill)-2
        while l<=r:
            if S == skill[l]+skill[r]:
                res += skill[l]*skill[r]
            else:
                return -1
            l+=1
            r-=1
        return res

