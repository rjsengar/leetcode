class Solution:
    def reverseParentheses(self, s: str) -> str:
        st=[]
        s1=""
        l=[]
        for i in range(len(s)):
            if s[i]==')':
                while(1):
                    k=st.pop()
                    if k=='(':
                        break
                    l.append(k)
                for j in l:
                    st.append(j)
                l=[]
            else:
                st.append(s[i])
        return "".join(st)
            
            
            


        