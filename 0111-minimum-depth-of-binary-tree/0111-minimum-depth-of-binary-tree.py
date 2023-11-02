# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # c=0
        # m=10000
        # if root ==None:
        #     return 0
        # def depth(root,c):
        #     nonlocal m
        #     if root.right==None and root.left==None:
        #         c+=1
        #         m=min(c,m)
        #     else:
        #         c+=1
        #         if root.left:
        #             depth(root.left,c)
        #         if root.right:
        #             depth(root.right,c)
        # depth(root,0)            
        # return m
        

        if root==None:
            return 0
        c=0
        m=100000000
        def helper(root,c):
            nonlocal m
            if root.left==None and root.right==None:
                c+=1
                m=min(c,m)
            else:
                c+=1
                if root.left:
                    helper(root.left,c)
                if root.right:
                    helper(root.right,c)
        helper(root,c)
        return m
        # q=[]
        # q.append(root)

        










