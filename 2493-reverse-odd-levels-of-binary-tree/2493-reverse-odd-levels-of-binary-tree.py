# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=[]
        a=[]
        if root!=None:
            q.append(root)
        i=0
        while(len(q)>0):
            t=[]
            l=len(q)
            while(l>0):
                n=q[0]
                q.remove(n)
                t.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                l-=1
            a.append(t[::-1])
        print(a)

        q=[]
        if root!=None:
            q.append(root)
        i=0
        while(len(q)>0):
            t=[]
            l=len(q)
            g=0
            while(l>0):
                n=q[0]
                q.remove(n)
                t.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                if i%2==0 and n.left and n.right:
                    n.left.val=a[i+1][g]
                    g+=1
                    n.right.val=a[i+1][g]
                    g+=1
                l-=1
            i+=1
        return root

        