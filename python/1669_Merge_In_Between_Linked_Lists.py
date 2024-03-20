# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next

        start = list1
        for _ in range(a - 1):
            start = start.next
        end = start.next
        for _ in range(b - a + 1):
            end = end.next
        
        start.next = list2
        tail2.next = end

        return list1