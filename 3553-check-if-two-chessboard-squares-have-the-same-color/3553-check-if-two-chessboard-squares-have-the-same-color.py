class Solution:
    def checkTwoChessboards(self, c1: str, c2: str) -> bool:
        s1='abcdefgh'
        d={}
        for i in range(len(s1)):
            d[s1[i]]=i
        if d[c1[0]]%2==d[c2[0]]%2:
            if int(c1[1])%2==int(c2[1])%2:
                return True
        else:
            if int(c1[1])%2!=int(c2[1])%2:
                return True

        return False
        
        

        