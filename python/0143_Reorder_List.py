# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
    
        # Locate and split at middle
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        head2 = slow.next
        slow.next = None

        # Reverse second half
        prev = None
        cur = head2
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        head2 = prev

        dummy = ListNode(0)
        cur = dummy

        while head:
            cur.next = head
            cur = cur.next
            head = head.next
            head, head2 = head2, head

        return dummy.next