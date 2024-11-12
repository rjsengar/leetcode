class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        ans=[]
        d={}
        p=queries[:]
        queries.sort()
        m=0
        for i in queries:
            j=0
            while(j<len(items)):
                if items[j][0]<=i:
                    m=max(items[j][1],m)
                    items.pop(0)
                    j-=1
                else:
                    break
                j+=1
                    

            ans.append(m)
        l1=[]
        for i in queries:
            d[i]=ans.pop(0)
        for i in p:
            l1.append(d[i])
        return l1