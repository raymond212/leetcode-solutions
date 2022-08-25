# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next
        if fast:
            slow = slow.next
        while reverse and reverse.val == slow.val:
            slow = slow.next
            reverse = reverse.next
        return not reverse