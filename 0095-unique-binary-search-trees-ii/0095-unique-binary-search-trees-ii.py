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
        for i in range(1,n+1):
            l.append(i)
        p=permutations(l)
        for i in list(p):
            i=list(i)
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
            ans=[]
            q=[h]
            while(q):
                le=len(q)
                while(le>0):
                    n=q[0]
                    q.remove(n)
                    ans.append(n.val)
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                    le-=1
            if ans not in l3:
                l1.append(h)
                l3.append(ans)
            
                        

        return l1
        