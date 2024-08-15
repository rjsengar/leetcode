# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import permutations
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        l=[]
        l1=[]
        l3=[]
        an=[]
        for i in range(1,n+1):
            l.append(i)
        def permute(a, l, r,ans): 
            if l == r:
                i=a[:]
                h=c=TreeNode(i[0])
                k=i[1:]
                for j in k:
                    c=h
                    while(1):
                        if j<c.val:
                            if c.left:
                                c=c.left
                            else:
                                c.left=TreeNode(j)
                                break
                        elif j>c.val:
                            if c.right:
                                c=c.right
                            else:
                                c.right=TreeNode(j)
                                break
                an=[]
                q=[h]
                while(q):
                    le=len(q)
                    while(le>0):
                        n=q[0]
                        q.remove(n)
                        an.append(n.val)
                        if n.left:
                            q.append(n.left)
                        if n.right:
                            q.append(n.right)
                        le-=1
                if an not in l3:
                    l1.append(h)
                    l3.append(an)
            else: 
                for i in range(l, r): 
                    a[l], a[i] = a[i], a[l] 
                    permute(a, l+1, r,ans) 
                    a[l], a[i] = a[i], a[l]
        permute(l,0,n,[])
            
        return l1
        