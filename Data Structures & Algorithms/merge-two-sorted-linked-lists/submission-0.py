# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        dummy = merged
        while list1 and list2:
            if list1.val < list2.val:
                temp = list1.next
                list1.next = None
                dummy.next = list1
                dummy = dummy.next
                list1 = temp
            else:
                temp = list2.next
                list2.next = None
                dummy.next = list2
                dummy = dummy.next
                list2 = temp
        dummy.next = list1 if list1 else list2
        return merged.next