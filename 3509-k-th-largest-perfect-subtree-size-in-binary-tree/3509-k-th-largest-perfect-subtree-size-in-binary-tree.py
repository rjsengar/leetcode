# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        def height(root):
            if root==None:
                return 0
            l=height(root.left)
            r=height(root.right)
            return (max(l,r))+1
        def tree(root,l):
            if root==None:
                return
            tree(root.left,l)
            l.append(root.val)
            tree(root.right,l)
        q=[root]
        l1=[]
        while(q):
            n=q[0]
            q.remove(n)
            l=[]
            tree(n,l)
            # print(l)
            p=height(n)
            # print(n.val,p)
            if len(l)==(2**p)-1:
                l1.append(len(l))
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        if len(l1)<k:
            return -1
        l1.sort(reverse=True)
        return l1[k-1]