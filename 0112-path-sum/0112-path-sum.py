# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        l=[]
        def tree(root,s):
            if root==None:
                return 
            s+=str(root.val)+'#'
            tree(root.left,s)
            tree(root.right,s)
            if root.left==None and root.right==None:
                l.append(s)
            s=s[:-1]
        tree(root,"")
        for i in l:
            i=i.split('#')
            i=i[:-1]
            c=0
            for j in i:
                c+=int(j)
            if c==targetSum:
                return True
        return False