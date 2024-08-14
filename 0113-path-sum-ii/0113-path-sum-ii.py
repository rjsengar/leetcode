# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        l=[]
        def tree(root,s):
            if root==None:
                return
            s+=str(root.val)+"#"
            tree(root.left,s)
            tree(root.right,s)
            if root.left==None and root.right==None:
                l.append(s)
            s=s[:-1]
        tree(root,"")
        l2=[]
        for i in l:
            i=i.split('#')
            i=i[:-1]
            l1=[]
            s1=0
            # print(i)
            for j in i:
                s1+=int(j)
                l1.append(int(j))
            if s1==targetSum:
                l2.append(l1)
        return l2

        