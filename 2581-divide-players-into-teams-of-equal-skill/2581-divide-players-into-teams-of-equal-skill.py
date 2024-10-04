class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n=len(skill)-1
        c1=0
        m=skill[0]+skill[-1]
        for i in range(len(skill)//2):
            if (skill[i]+skill[n-i])!=m:
                return -1
            else:
                c1+=(skill[i]*skill[n-i])
        return c1
        