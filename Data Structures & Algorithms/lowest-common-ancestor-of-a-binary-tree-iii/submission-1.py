# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.parent = None
# """

# class Solution:
#     def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
#         my_set: Set[Node] = set()
#         """
#         T: O(n), S: O
#         """
#         while p != None:
#             my_set.add(p)
#             p = p.parent
#         while q != None:
#             if q in my_set:
#                 return q
#             q = q.parent
#         return None
        
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1 = p
        q1 = q

        while p1 != q1:

            p1 = q if p1 is None else p1.parent
            q1 = p if q1 is None else q1.parent
        return p1

