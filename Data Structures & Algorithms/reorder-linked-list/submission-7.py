# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        curr = mid
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr = head
        rev_half = prev
        while rev_half:
            curr_nxt = curr.next
            rev_nxt = rev_half.next
            curr.next = rev_half
            rev_half.next = curr_nxt
            rev_half = rev_nxt
            curr = curr_nxt
        

