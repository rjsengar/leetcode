# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d={}
        d1={}
        d2={}
        h=0
        for i in descriptions:
            if i[2]==1:
                d1[i[0]]=i[1]
            else:
                d2[i[0]]=i[1]
            y=i[1]
            d[y]=1
        for i in descriptions:
            if i[0] not in d:
                h=i[0]
                break
        h1=c1=TreeNode(h)
        q=[h1]
        while(q):
            l=len(q)
            while(l>0):
                n=q[0]
                # print(n.val)
                q.remove(n)
                if n.val in d1:
                    x=TreeNode(d1[n.val])
                    n.left=x
                    q.append(x)
                if n.val in d2:
                    y=TreeNode(d2[n.val])
                    n.right=y
                    q.append(y)
                l-=1
        return c1

                
        