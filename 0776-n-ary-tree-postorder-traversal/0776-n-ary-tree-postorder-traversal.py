"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root==None:
            return []
        l=[]
        s=[root]
        d={}
        while(s):
            a=s.pop()
            if a not in d:
                l.append(a.val)
                d[a]=1
            for i in a.children:
                s.append(i)
        return l[::-1]

        