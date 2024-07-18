# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if distance==0 or root.left==None and root.right==None:
            return 0
        q=[root]
        a=[]
        d1={}
        d={}
        while(q):
            l=len(q)
            while(l>0):
                n=q[0]
                q.remove(n)
                if n not in d1:
                    d1[n]=[]
                if n.left:
                    d1[n].append(n.left)
                    if n.left not in d1:
                        d1[n.left]=[n]
                    else:
                        d1[n.left].append(n)
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                    d1[n].append(n.right)
                    if n.right not in d1:
                        d1[n.right]=[n]
                    else:
                        d1[n.right].append(n)
                if n.left==None and n.right==None:
                    d[n]=1
                l-=1
        a=[]
        c1=0
        for i in d:
            a.append(i)
        for i in a:
            # print(i)
            d2={}
            q=[i]
            c=0
            while(q):
                l=len(q)
                while(l>0):
                    n=q[0]
                    q.remove(n)
                    if n in d and c<=distance and n!=i:
                        c1+=1
                        # print(i.val,n.val)
                    for j in d1[n]:
                        if j not in d2:
                            q.append(j)
                            d2[j]=1
                    l-=1
                c+=1
                # if c>distance:
                #     break
        # print(d1)
        # print(d)
        return c1//2

        
        return 1
        
            
            
        