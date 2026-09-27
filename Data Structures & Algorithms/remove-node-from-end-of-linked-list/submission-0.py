# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        removal_idx = length - n
        if removal_idx == 0:
            return head.next
        curr = dummy = head
        i = 0
        while dummy:
            if i == removal_idx - 1:
                dummy.next = dummy.next.next
            dummy = dummy.next
            i += 1
        return curr