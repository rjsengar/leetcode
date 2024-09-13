class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        l=[]
        l1=[]
        k=0
        for i in arr:
            k^=i
            l1.append(k)
        for i,j in queries:
            s=0
            if i==0:
                l.append(l1[j])
            else:
                p=l1[j]^l1[i]
                p^=arr[i]
                l.append(p)
            # for j in range(i,j+1):
            #     s^=arr[j]
            # l.append(s)
        return l
        