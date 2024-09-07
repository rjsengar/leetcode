# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        l1=[]
        def dfs(root,s):
            if root==None:
                return
            s+=str(root.val)+"#"
            dfs(root.left,s)
            dfs(root.right,s)
            if root.left==None and root.right==None:
                l1.append(s)
                s=s[:-1]



        a=head.val
        curr=head
        s1=""
        while(curr):
            s1+=str(curr.val)+'#'
            curr=curr.next
        q=[root]
        l=[]
        while(q):
            n=q[0]
            q.remove(n)
            if n.val==a:
                l.append(n)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        for i in l:
            dfs(i,"")
        for i in l1:
            if s1 in i:
                return True
        return False




        