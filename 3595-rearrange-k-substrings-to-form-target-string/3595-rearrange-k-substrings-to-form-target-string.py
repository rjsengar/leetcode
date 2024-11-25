class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        le=len(s)
        a=le//k
        i=0
        l1=[]
        l2=[]
        while(i<len(s)-a+1):
            l1.append(s[i:i+a])
            l2.append(t[i:i+a])
            i+=a
        l1.sort()
        l2.sort()
        if l1==l2:
            return True
        return False
        