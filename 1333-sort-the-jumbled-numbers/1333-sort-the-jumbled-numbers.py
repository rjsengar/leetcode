class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d={}
        d3={}
        d4={}
        l=[]
        k=0
        for i in nums:
            d[i]=0
        for i in nums:
            s=0
            for j in str(i):
                s=s*10+(mapping[int(j)])
            d3[k]=s
            d4[k]=i
            k+=1
        # print(d3,d4)
        d1={}
        for key in sorted(d3, key=d3.get):
            d1[key] = d3[key]
        for i in d1:
            l.append(d4[i])
        
        return l
        