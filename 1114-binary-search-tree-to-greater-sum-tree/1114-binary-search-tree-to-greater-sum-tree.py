# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        l=[]
        def tree(root,l):
            if root==None:
                return
            tree(root.left,l)
            l.append(root.val)
            tree(root.right,l)
        tree(root,l)
        s=0
        l1=[]
        for i in l[::-1]:
            s+=i
            l1.append(s)
        l1=l1[::-1]
        # print(l1)
        # print(l)
        q=[]
        if root:
            q=[root]
        while(q):
            le=len(q)
            while(le>0):
                n=q[0]
                q.remove(n)
                k=l.index(n.val)
                n.val=l1[k]
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                le-=1

        return root