class MyCircularDeque:

    def __init__(self, k: int):
        self.k=k
        self.l=[]
        
    def insertFront(self, value: int) -> bool:
        if (self.isFull()):
            return False
        else:
            self.l.insert(0,value)
            return True
        

    def insertLast(self, value: int) -> bool:
        if (self.isFull()):
            return False
        else:
            self.l.append(value)
            return True
        

    def deleteFront(self) -> bool:
        if (self.isEmpty()):
            return False
        else:
            self.l.pop(0)
            return True
        

    def deleteLast(self) -> bool:
        if (self.isEmpty()):
            return False
        else:
            self.l.pop(-1)
            return True
        

    def getFront(self) -> int:
        if (self.isEmpty()):
            return -1
        else:
            a=self.l[0]
            return a

    def getRear(self) -> int:
        if (self.isEmpty()):
            return -1
        else:
            a=self.l[-1]
            return a
        

    def isEmpty(self) -> bool:
        if len(self.l)==0:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.l)==self.k:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()