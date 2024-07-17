# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        d={}
        l1=[]
        for i in to_delete:
            d[i]=1
        def tree(root,d):
            if root==None:
                return 
            root.left=tree(root.left,d)
            root.right=tree(root.right,d)
            if root.val in d:
                if root.left:
                    l1.append(root.left)
                if root.right:
                    l1.append(root.right)
                return None
            return root
        tree(root,d)
        if root.val not in d:
            l1.append(root)
        return l1
        # q=[root]
        # a=TreeNode(0)
        # l1=[]
        # while(q):
        #     l=len(q)
        #     while(l>0):
        #         n=q[0]
        #         q.remove(n)
        #         if n.val in to_delete:
        #             n.val=0
        #         if n.left:
        #             q.append(n.left)
        #         if n.right:
        #             q.append(n.right)
        #         l-=1
        # if root.val==0:
        #     q=[root]
        #     while(q):
        #         l=len(q)
        #         while(l>0):

        