from itertools import combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        s='abcdefghijklmnopqrstuvwxyz'
        d={}
        for i in range(2,10):
            d[i]=[]
        for i in range(len(s)):
            if i<=2:
                d[2].append(s[i])
            elif i<=5:
                d[3].append(s[i])
            elif i<=8:
                d[4].append(s[i])
            elif i<=11:
                d[5].append(s[i])
            elif i<=14:
                d[6].append(s[i])
            elif i<=18:
                d[7].append(s[i])
            elif i<=21:
                d[8].append(s[i])
            elif i<=25:
                d[9].append(s[i])
        l=[]
        l1=[]
        for i in digits:
            if i not in '*0#1' and i:
                l+=d[int(i)]
        n=len(digits)
        if n==1:
            return d[int(digits[0])]
        if n==2:
            for i in d[int(digits[0])]:
                for j in d[int(digits[1])]:
                    l1.append(i+j)
        if n==3:
            for i in d[int(digits[0])]:
                for j in d[int(digits[1])]:
                    for k in d[int(digits[2])]:
                        l1.append(i+j+k)
        if n==4:
            for i in d[int(digits[0])]:
                for j in d[int(digits[1])]:
                    for k in d[int(digits[2])]:
                        for t in d[int(digits[3])]:
                            l1.append(i+j+k+t)
        return l1
        


        