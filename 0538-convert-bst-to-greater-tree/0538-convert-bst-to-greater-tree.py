# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        l=[]
        d={}
        def tree(root):
            if root==None:
                return 
            tree(root.left)
            l.append(root.val)
            tree(root.right)
        tree(root)
        # print(l)
        c=0
        for i in range(len(l)-1,-1,-1):
            c+=l[i]
            d[l[i]]=c
        q=[]
        if root:
            q=[root]
        while(q):
            l=len(q)
            while(l>0):
                n=q[0]
                n.val=d[n.val]
                q.remove(n)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                l-=1
        
        return root
            
        