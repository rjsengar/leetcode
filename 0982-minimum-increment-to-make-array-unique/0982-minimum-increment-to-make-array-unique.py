class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=[]
        d1={}
        c=0
        p=max(nums)+(n-len(list(set(nums))))
        for i in range(1,p+1):
            if i not in d:
                l.append(i)
        # print(l)
        for i in nums:
            if i not in d1:
                d1[i]=1
            else:
                # print(i)
                while(l):
                    k=l.pop(0)
                    if k>i:
                        c+=(k-i)
                        break
        return c



            
        