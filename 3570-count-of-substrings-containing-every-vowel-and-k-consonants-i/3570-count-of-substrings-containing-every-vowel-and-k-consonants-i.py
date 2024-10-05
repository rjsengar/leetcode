class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vo='aeiou'
        d={}
        c2=0
        for i in vo:
            d[i]=0
        for i in range(len(word)-4-k):
            c=0
            c1=0
            # print(d)
            for j in range(i,len(word)):
                c1=0
                if word[j] in d:
                    d[word[j]]=1
                else:
                    c+=1
                for t in d:
                    if d[t]:
                        c1+=1
                if c1==5 and c==k:
                    c2+=1
                if c>k:
                    break
                
            for t in d:
                d[t]=0
        return c2


        