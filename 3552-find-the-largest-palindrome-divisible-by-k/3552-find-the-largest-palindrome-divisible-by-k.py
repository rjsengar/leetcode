import sys

# Increase the limit for integer string conversion
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        sys.set_int_max_str_digits(1000000)
        if k==3 or k==9 or k==1:
            return n*'9'
        if k==2:
            if n<=1:
                return '8'*n
            else:
                return '8'+'9'*(n-2)+'8'
        if k==6:
            if n<=2:
                return '6'*n
            else:
                s1='8'+'9'*(n-2)+'8'
                s1=list(s1)
                p=(2*8)+(9*(n-2))
                # print(p%3)
                if p%3!=0:
                    k=p%3
                    if n%2!=0:
                        s1[n//2]=str(9-k)
                    else:
                        if k==1:
                            s1[n//2]=str(9-k-1)
                            s1[(n//2)-1]=str(9-k-1)
                        else:
                            s1[n//2]=str(9-k)
                            s1[(n//2)-1]=str(9-k)
                return "".join(s1)
        if k==8:
            if n<=6:
                return '8'*n
            else:
                return '888'+('9'*(n-6))+'888' 
             
                
        if k==5:
            if n<=2:
                return n*'5'
            else:
                return '5'+(n-2)*'9'+'5'
        if k==7:
            if n<=2:
                return '7'*n
            p=list('9'*n)
            if int("".join(p))%7==0:
                return "".join(p)
            if n%2!=0:
                t=8
                while(t>0):
                    p[n//2]=str(t)
                    t-=1
                    if int("".join(p))%k==0:
                        return "".join(p)
            else:
                t=8
                while(t>0):
                    p[n//2]=str(t)
                    p[(n//2)-1]=str(t)
                    t-=1
                    if int("".join(p))%k==0:
                        return "".join(p)


            # while(True):
            #     if x%7==0 and p==p[::-1]:
            #         return p
            #     x=x-(int(p[-1]))*2
            #     p=str(x)
        if k==4:
            if n<=4:
                return '8'*n
            else:
                return '88'+('9'*(n-4))+'88'

        return '1'
        