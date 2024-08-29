class Solution:
    def nearestPalindromic(self, n: str) -> str:
        
        # n=int(n)
        a=int(n)//2
        n1=int(n)
        n2=int(n)
        li=[]
        c=1
        if len(n)==1:
            if n=='0':
                return '1'
            return str(int(n)-1)
        while(c<=100):
            s=str(n1-c)
            s1=str(n2+c)
            if s==s[::-1]:
                li.append(int(s))
                break
            if s1==s1[::-1]:
                li.append(int(s1))
                break
            c+=1
        # print(li)
        # return min(l)
        n2=int(n2)
        l=len(n)
        l1=len(n)
        l//=2
        s1=int(n[:l])
        if l1%2!=0:
            l+=1
        s2=int(n[l:])
        if l1%2!=0:
            k=int(n[l1//2])
            if s1==s2:
                if k-1>=0 and (li==[] or (abs(min(li)-n2))>abs(int(str(s1)+str(k-1)+str(s2))-n2)):
                    return str(s1)+str(k-1)+str(s2)
                else:
                    li.append(int(str(s1)+str(k+1)+str(s2)))
            n2=int(n)
            a=str(s1-1)
            b=str(s1+1)
            c=str(s1)
            a=int(a+str(k)+a[::-1])
            b=int(b+str(k)+b[::-1])
            c=int(c+str(k)+c[::-1])
            # print(a,b,c)

            li.append(a)
            li.append(b)
            li.append(c)
            if k-1>=0:
                a=str(s1-1)
                b=str(s1+1)
                c=str(s1)
                a=int(a+str(k-1)+a[::-1])
                b=int(b+str(k-1)+b[::-1])
                c=int(c+str(k-1)+c[::-1])
                # print(a,b,c)
                li.append(a)
                li.append(b)
                li.append(c)
            # print(li)
        else:
            l=len(n)//2
            s1=int(n[:l])
            s2=int(n[l:])
            n2=int(n)
            a=str(s1-1)
            b=str(s1+1)
            c=str(s1)
            a=int(a+a[::-1])
            b=int(b+b[::-1])
            c=int(c+c[::-1])
            # print(a,b,c)
            li.append(a)
            li.append(b)
            li.append(c)
        li.sort()
        
        k=n2
        m=n2
        for i in li:
            if str(i)!=n and i!=0:
                if abs(int(i)-n2)<=m:
                    if m==abs(int(i)-n2):
                        if i<k:
                            k=i
                    else:
                        k=i
                    m=abs(int(i)-n2)
        return str(k)
        return str(min(li))


            
        