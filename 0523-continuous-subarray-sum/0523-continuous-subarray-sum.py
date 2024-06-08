class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s=0
        l=[]
        m=[]
        d={}
        for i in range(len(nums)):
            s+=nums[i]
            if s%k==0 and i>=1:
                return True
            l.append(s)
        for i in l:
            m.append(i%k)
        for i in range(len(m)):
            d[m[i]]=i
        print(d)
        j=0
        for i in d:
            if i==0 and d[i]>1:
                return True
        for i in range(len(m)):
            if abs(d[m[i]]-i)>1:
                return True
            
        return False



                