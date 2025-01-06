class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l=[]
        l1=[]
        for i in range(len(boxes)):
            if boxes[i]=='1':
                l.append(i)
        for i in range(len(boxes)):
            c=0
            for j in l:
                c+=abs(i-j)
            l1.append(c)
        return l1
        