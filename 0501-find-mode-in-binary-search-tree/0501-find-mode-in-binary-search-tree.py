# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        q=[]
        a=[]
        d={}
        l1=[]
        if root!=None:
            q.append(root)
        while(len(q)):
            t=[]
            l=len(q)
            while(l):
                n=q[0]
                q.remove(n)
                t.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                l-=1
            a.append(t)
        l1=[]
        l2=[]
        for i in a:
            for j in i:
                l1.append(j)
        for i in l1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        m=0
        for i in d:
            m=max(m,d[i])
        l1=list(set(l1))
        for i in l1:
            if d[i]==m:
                l2.append(i)
        

        if l2==[]:
            return [0]
        return l2
        