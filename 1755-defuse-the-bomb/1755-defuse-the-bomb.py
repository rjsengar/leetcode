class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l1=[]
        if k==0:
            return [0]*len(code)
        if k<0:
            for i in range(len(code)):
                s=abs(k)
                c=0
                while(s):
                    c+=code[i-s]
                    s-=1
                l1.append(c)
        else:
            for i in range(len(code)):
                s=abs(k)
                c=0
                while(s):
                    c+=code[(i+s)%len(code)]
                    s-=1
                l1.append(c)

        return l1
        