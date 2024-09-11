# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        L = 0
        cur = head
        while cur:
            cur = cur.next
            L += 1
        partL = L // k
        rem = L % k

        res = []
        for i in range(k):
            res.append(head)
            curL = partL + (1 if i < rem else 0)
            if curL == 0:
                continue
            for _ in range(curL - 1):
                head = head.next
            tmp = head
            head = head.next
            tmp.next = None
        
        return res
