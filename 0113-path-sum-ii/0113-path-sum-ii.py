# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        l=[]
        l2=[]
        def tree(root,l):
            if root==None:
                return
            l.append(root.val)
            tree(root.left,l)
            tree(root.right,l)
            if root.left==None and root.right==None:
                if sum(l)==targetSum:
                    l2.append(l[:])    
            l.pop()
        tree(root,l)
        return l2

        