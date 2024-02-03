# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        l = 1
        tail = head
        while tail.next:
            tail = tail.next
            l += 1

        k = k % l
        if k == 0:
            return head

        cur = head
        for _ in range(l - k - 1):
            cur = cur.next

        old_head = head
        new_head = cur.next
        tail.next = old_head
        cur.next = None

        return new_head

