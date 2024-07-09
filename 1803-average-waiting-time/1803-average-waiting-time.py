class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        x=0
        c=0
        k=customers[0][0]
        t=0
        for i,j in customers:
            if i<k:
                c+=(k-i)
                c+=abs((j))
            else:
                c+=(j)
            k+=j
            k=max(k,i+j)
            t+=1
        return c/len(customers)
        