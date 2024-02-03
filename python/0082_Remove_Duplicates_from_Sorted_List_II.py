# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        while cur:
            delete = False
            while cur.next and cur.next.next and cur.next.next.val == cur.next.val:
                cur.next = cur.next.next
                delete = True
            if delete:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next