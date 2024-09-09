# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        arr = [[-1] * n for _ in range(m)]
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dirIdx = 0
        r = c = 0

        while head:
            arr[r][c] = head.val
            head = head.next
            nr, nc = r + dirs[dirIdx][0], c + dirs[dirIdx][1]
            if 0 <= nr < m and 0 <= nc < n and arr[nr][nc] == -1:
                r, c = nr, nc
            else:
                dirIdx = (dirIdx + 1) % 4
                r, c = r + dirs[dirIdx][0], c + dirs[dirIdx][1]

        return arr