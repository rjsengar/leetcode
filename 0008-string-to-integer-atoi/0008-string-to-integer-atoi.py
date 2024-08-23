class Solution:
    def myAtoi(self, s: str) -> int:
        s1=""
        c=0
        p=0
        k=0
        if s=="":
            return 0
        for i in s:
            if i=='+' and k==0:
                k+=1
                p+=1
                continue
            if i==' ' and p==0:
                continue
            elif i.isdigit():
                if s1=="" and i=='0':
                    p+=1
                    k+=1
                    continue
                s1+=i
                k+=1
                p+=1
            elif i=="-" and k==0:
                p+=1
                k+=1
                c+=1
            else:
                break
        if s1=="":
            return 0
        if c==1:
            if -(int(s1))<-2**31:
                return -(2**31)
            return -(int(s1))
        if int(s1)>2**31-1:
            return 2**31-1
        return int(s1)