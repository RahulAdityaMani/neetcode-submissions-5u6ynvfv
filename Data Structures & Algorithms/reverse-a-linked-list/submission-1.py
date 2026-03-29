# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        reversed_nodes = None
        while head is not None:
            next_nodes = head.next
            head.next = reversed_nodes
            reversed_nodes = head
            head = next_nodes
        return reversed_nodes