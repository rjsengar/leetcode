class MyCalendar:

    def __init__(self):
        self.l=[]
        

    def book(self, start: int, end: int) -> bool:
        if len(self.l)==0:
            self.l.append([start,end-1])
            return True
        temp=True
        for i in self.l:
            if (i[0]<=start and i[1]>=start) or (i[0]<=end-1 and i[1]>=end-1):
                
                return False
            if start<i[0] and end>i[1]:
                return False
        self.l.append([start,end-1])
        return True

        # print(self.m2,start,end)
        

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)