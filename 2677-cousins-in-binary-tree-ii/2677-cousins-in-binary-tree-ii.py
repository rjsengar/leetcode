# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=[]
        a=[]
        if root:
            q=[root]
        while(q):
            l=len(q)
            c=0
            while(l>0):
                n=q[0]
                q.remove(n)
                c+=n.val
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                l-=1
            a.append(c)
        # print(a)
        q=[root]
        root.val=0
        j=1
        while(q):
            l=len(q)
            c1=0
            while(l>0):
                n=q[0]
                q.remove(n)
                if n.left and n.right:
                    c1=n.left.val+n.right.val
                    n.left.val=(a[j]-c1)
                    n.right.val=(a[j]-c1)
                    q.append(n.left)
                    q.append(n.right)
                else:
                    if n.right:
                        c1=n.right.val
                        n.right.val=(a[j]-c1)
                        q.append(n.right)
                        
                    elif n.left:
                        c1=n.left.val
                        n.left.val=a[j]-c1
                        q.append(n.left)
                    
                l-=1
            j+=1
        return root

        