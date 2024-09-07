class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        a=str(num1)
        b=str(num2)
        c=str(num3)
        m=max(len(a),len(b),len(c))
        a=(m-len(a))*'0'+a
        b=(m-len(b))*'0'+b
        c=(m-len(c))*'0'+c
        s1=""
        l=[a,b,c]
        for i in range(len(l[0])):
            m1=100000
            for j in range(len(l)):
                m1=min(m1,int(l[j][i]))
            s1+=str(m1)
        return int(s1)