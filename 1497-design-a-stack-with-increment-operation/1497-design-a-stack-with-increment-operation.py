class CustomStack:

    def __init__(self, maxSize: int):
        self.m=maxSize
        self.s=[]

    def push(self, x: int) -> None:
        if len(self.s)<self.m:
            self.s.append(x)

    def pop(self) -> int:
        if self.s:
            return self.s.pop()
        return -1
        

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i<len(self.s):
                self.s[i]+=val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)