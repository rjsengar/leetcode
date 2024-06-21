class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        dk=max(date1,date2)
        dp=min(date1,date2)
        d1=dk.split('-')
        d2=dp.split('-')
        d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        y1=int(d1[0])
        y2=int(d2[0])
        x1=y1
        x2=y2
        m1=int(d1[1])
        m2=int(d2[1])
        da1=int(d1[2])
        da2=int(d2[2])
        c=0
        k1=m1
        k2=m2
        if y1==y2 and m1==m2:
            return abs(da1-da2)
        y1-=1
        while(y2<y1):
            y2+=1
            if (y2%400==0 or (y2%100!=0 and y2%4==0)):
                c+=366
            else:
                c+=365
        if x1!=x2:
            m2+=1
            m1-=1
            while(m2<13):
                c+=d[m2]
                if m2==2 and (x2%400==0 or (x2%100!=0 and x2%4==0)):
                    c+=1
                m2+=1
            while(m1>0):
                c+=d[m1]
                if m1==2 and (x1%400==0 or (x1%100!=0 and x1%4==0)):
                    c+=1
                m1-=1
            if int(d2[1])==2 and (x2%400==0 or (x2%100!=0 and x2%4==0)):
                c+=1
            c+=abs(d[int(d2[1])]-da2)
            c+=da1
        return c
        


        
        

        