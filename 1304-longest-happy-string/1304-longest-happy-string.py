from queue import PriorityQueue
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        l=[]
        if a:
            l.append([a,'a'])
        if b:
            l.append([b,'b'])
        if c:
            l.append([c,'c'])
        l.sort(reverse=True)
        s=""
        while(1):
            s1=s
            for i in range(len(l)):
                if s=="" or s[-1]!=l[i][1]:
                    if l[i][0]>=2 and i==0:
                        s+=l[i][1]*2
                        l[i][0]-=2
                        break
                    else:
                        if l[i][0]:
                            s+=l[i][1]
                            l[i][0]-=1
                            break
            l.sort(reverse=True)
            # print(l)
            if s==s1:
                break
        return s


        # while(len(l)>1):
        #     if l[0][0]>=2:
        #         s+=l[0][1]*2
        #         l[0][0]-=2
        #     else:
        #         if l[0][0]==1:
        #             s+=l[0][1]
        #             l[0][0]-=1
        #             l.pop(0)
        #     if l[-1][0]>=2:
        #         s+=l[-1][1]*2
        #         l[-1][0]-=2
        #     else:
        #         if l[-1][0]==1:
        #             s+=l[-1][1]
        #             l.pop()
        # for i in l:
        #     if s[-1]!=i[1]:
        #         if i[0]>=2:
        #             s+=i[1]*2
        #         else:
        #             s+=i[1]
        #             i[1]-=1
            
                
                    
        return s  
            
        # q=PriorityQueue()
        for i in l:
            q.put(i)
        k=1
        while(q.qsize()):
            k=1
            a1=q.get()
            if abs(a[0])>=2:
                s+=a[1]*2
                a[0]=abs(a[0])-2
            elif abs(a[0])==1:
                s+=a[1]
                k=0
            b1=q.get()
            if abs(b1[0])>=2:
                s+=b1[1]*2
                b1[0]=abs(b1[0])-2
            elif abs(b1[0])==1:
                s+=b1[1]
                k=0


  
            break
        return ""
        

        # t1=1
        # t2=1
        # t3=1
        # s=""
        # while(1):
        #     s1=s
        #     if t1:
        #         if l[0][0]>=2:
        #             s+=l[0][1]*2
        #             t1=0
        #             t2=1
        #             t3=1
        #         else:
        #             s+=l[0][1]
        #             t1=0
        #             t2=1
        #             t3=1
        #     elif t2:
        #         if l[1][0]>=2:
        #             s+=l[1][1]*2
        #             t2=0
        #             t1=1
        #             t3=1
        #         else:
        #             s+=l[1][1]
        #             t2=0
        #             t1=1
        #             t3=1
        #     else:
        #         if t3 and  l[2][0]>=2:
        #             s+=l[2][1]*2
        #             t3=0
        #             t1=1
        #             t2=1
        #         elif t3:
        #             s+=l[2][1]
        #             t3=0
        #             t1=1
        #             t2=1
        #     if s1==s:
        #         break
        # return s

        
        