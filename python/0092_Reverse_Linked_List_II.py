# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        cur = dummy.next

        for _ in range(left - 1):
            tmp = cur
            cur = cur.next
            prev = tmp
        
        node1 = prev
        node2 = cur

        for _ in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        node2.next = cur
        node1.next = prev

        return dummy.next