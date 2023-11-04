# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        a=[]
        q=[]
        c=1
        if root:
            q.append(root)
        while(len(q)):
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
            if c%2!=0:
                a.append(t)
            else:
                a.append(t[::-1])
            if t==root.val:
                continue
            c+=1

        return a
        
        