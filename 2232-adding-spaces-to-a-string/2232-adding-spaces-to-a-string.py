class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        c=0
        s1=""
        for i in range(len(s)):
            if c<len(spaces) and i==spaces[c]:
                s1+=" "
                s1+=s[i]
                c+=1
            else:
                s1+=s[i]
        return s1
        