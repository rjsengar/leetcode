# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int: 
        q=[root]
        a=[]
        while(q):
            l=len(q)
            t=[]
            while(l>0):
                n=q[0]
                q.remove(n)
                t.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                l-=1
            a.append(t)
        c=0
        # print(a)
        for i in a:
            if i==sorted(i):
                continue
            s=sorted(i)
            t=i[:]
            k=0
            d={}
            for j in range(len(s)):
                d[t[j]]=j
            # print(d)
            while(k<len(s)):
                if t[k]!=s[k]:
                    c+=1
                    p=d[s[k]]
                    g=t[k]
                    t[k],t[p]=t[p],t[k]
                    d[g]=p
                    d[s[k]]=k
                k+=1
        return c
                
        