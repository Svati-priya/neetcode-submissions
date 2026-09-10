# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        while head != None:
            values.append(head.val)
            head = head.next
        i = 0 
        j = len(values) - 1
        max_value = float('-inf')
        while i < j:
            candidate = values[i] + values[j]
            max_value = max(max_value, candidate)
            i += 1
            j -= 1
        return max_value
        