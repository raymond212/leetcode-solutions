# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        
        while (cur.next and cur.next.next):
            tmp1 = cur.next
            tmp2 = tmp1.next
            cur.next, tmp1.next, tmp2.next = tmp2, tmp2.next, tmp1
            
            cur = tmp1
        
        return dummy.next