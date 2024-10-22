# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q=[]
        a=[]
        if root:
            q.append(root)
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
        if len(a)<k:
            return -1
        a.sort(reverse=True)
        return a[k-1]
        