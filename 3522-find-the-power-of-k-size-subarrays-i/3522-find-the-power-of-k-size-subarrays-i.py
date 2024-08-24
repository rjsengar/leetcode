class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l=[]
        if k>len(nums):
            return [-1]
        s=nums[:k]
        s1=sorted(s)
        if s==sorted(s) and len(list(set(s)))==len(s) and s1[-1]-s1[0]==k-1:
            l.append(s1[-1])
        else:
            l.append(-1)
        for i in range(k,len(nums)):
            s.pop(0)
            s.append(nums[i])
            s1=sorted(s)
            if s==sorted(s) and len(list(set(s)))==len(s) and s1[-1]-s1[0]==k-1:
                l.append(s1[-1])
            else:
                l.append(-1)
        return l


        
        