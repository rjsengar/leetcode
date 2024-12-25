# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        q=[root]
        a=[]
        while(q):
            l=len(q)
            m=-100000000000000
            while(l>0):
                n=q[0]
                q.remove(n)
                m=max(m,n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                l-=1
            a.append(m)
        return a