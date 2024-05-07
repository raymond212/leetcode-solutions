# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(node):
            if not node:
                return 0
            new_val = (2 * node.val + dfs(node.next))
            node.val = new_val % 10
            return new_val // 10
        
        return head if dfs(head) == 0 else ListNode(val=1, next=head) 