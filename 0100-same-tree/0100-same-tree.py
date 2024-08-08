# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(p,q):
            if p==None and q==None:
                return True
            if p!=None and q!=None:
                if p.val==q.val:
                    s=traverse(p.left,q.left)
                    t=traverse(p.right,q.right)
                    if s and t:
                        return True
            return False
        return traverse(p,q)
        
        
        