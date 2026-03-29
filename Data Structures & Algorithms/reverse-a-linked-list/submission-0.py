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
        curr_node = head
        while curr_node is not None:
            next_nodes = curr_node.next
            curr_node.next = reversed_nodes
            reversed_nodes = curr_node
            curr_node = next_nodes
        return reversed_nodes