class Solution:
    def printVertically(self, s: str) -> List[str]:
        res=" "
        x=s.split()
        # print(s)
        # print(len(s))
        c=0
        j=0
        ans=[]
        ma,mi=0,0
        for i in x:
            ma=max(len(i),ma)
            mi=min(len(i),mi)
        # print(ma,mi)
        while(c<ma):
            res=[]
            for i in range(len(x)):
                if c<len(x[i]) and x[i][c]!=" ":
                    res.append(x[i][c])       
                else:
                    res.append(" ")
            c+=1
            if c>mi:
                while(res):
                    if res[-1]==" ":
                        res.pop()
                    else:
                        break
            ans.append("".join(res))
        # print(ans)
        return ans
        

