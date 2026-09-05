"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        my_set: Set[Node] = set()
        while p != None:
            my_set.add(p)
            p = p.parent
        while q != None:
            if q in my_set:
                return q
            q = q.parent
        return None
        