class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m2=0
        m1=10000000
        m=0
        l=[]
        l1=[]
        k=0
        for i in arrays:
            l.append([i[-1],k])
            k+=1
        k=0
        for i in arrays:
            l1.append([i[0],k])
            k+=1
        l1.sort()
        l.sort(reverse=True)
        for i in range(len(l1)):
            if l1[0][1]!=l[i][1] or l[0][1]!=l1[i][1]:
                return max(abs(l1[i][0]-l[0][0]),abs(l1[0][0]-l[i][0]))
        return 0
        
        