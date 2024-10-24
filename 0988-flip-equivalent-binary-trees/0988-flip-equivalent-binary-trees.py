# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        q=[]
        d={}
        if root1:
            q=[root1]
        while(q):
            n=q[0]
            q.remove(n)
            d[n.val]=[]
            if n.left:
                d[n.val].append(n.left.val)
                q.append(n.left)
            if n.right:
                d[n.val].append(n.right.val)
                q.append(n.right)
        # print(d)
        if d!={} and root2==None:
            return False 
        if root2:
            q=[root2]
        while(q):
            l1=[]
            n=q[0]
            q.remove(n)
            if n.val not in d:
                return False
            if n.left:
                l1.append(n.left.val)
                q.append(n.left)
            if n.right:
                l1.append(n.right.val)
                q.append(n.right)
            if l1!=d[n.val] and l1[::-1]!=d[n.val]:
                return False
        return True

        