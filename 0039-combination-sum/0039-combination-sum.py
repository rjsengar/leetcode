from itertools import combinations
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        q=[]
        l1=[]
        l2=[]
        candidates.sort()
        for i in candidates:
            q.append([i])
        while(q):
            l=len(q)
            while(l>0):
                n=q[0]
                q.remove(n)
                if sum(n)==target:
                    l1.append(n)
                else:
                    for i in candidates:
                        if sum(n)+i<=target:
                            q.append(n+[i])
                l-=1
        for i in range(len(l1)):
            l1[i].sort()
            if l1[i] not in l2:
                l2.append(l1[i])
        l2.sort()
        return l2

