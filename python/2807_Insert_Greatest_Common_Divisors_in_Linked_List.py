# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next:
            gcd_node = ListNode(gcd(cur.val, cur.next.val))
            cur.next, gcd_node.next = gcd_node, cur.next
            cur = cur.next.next
        return head