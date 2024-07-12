class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        st=[]
        c1=0
        c2=0
        s1=s
        for i in s1:
            if st and st[-1]=='b' and i=='a':
                c1+=1
                st.pop()
            else:
                st.append(i)
        s1="".join(st)
        st=[]
        for i in s1:
            if st and st[-1]=='a' and i=='b':
                c2+=1
                st.pop()
            else:
                st.append(i)
        s2=s
        c3,c4=0,0
        st1=[]
        for i in s2:
            if st1 and st1[-1]=='a' and i=='b':
                c3+=1
                st1.pop()
            else:
                st1.append(i)
        s2="".join(st1)
        # print(s2)
        st1=[]
        for i in s2:
            if st1 and st1[-1]=='b' and i=='a':
                c4+=1
                st1.pop()
            else:
                st1.append(i)
        # print(c3,c4)
        a=(c1*y)+(c2*x)
        b=(c3*x)+(c4*y)
        # print(a,b)
        return max(a,b)


        