# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None
        
        fast = head

        for i in range(n):
            fast = fast.next
        
        dummy = ListNode()
        dummy.next = head
        slow = dummy

        while fast:
            fast = fast.next
            slow = slow.next
        
        to_be_removed = slow.next
        to_stay = to_be_removed.next

        slow.next = to_stay
        to_be_removed.next = None

        return dummy.next