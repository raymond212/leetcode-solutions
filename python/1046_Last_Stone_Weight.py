class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapify(stones)

        while len(stones) > 1:
            x, y = -heappop(stones), -heappop(stones)
            if x < y:
                heappush(stones, -(y - x))
            elif x > y:
                heappush(stones, -(x - y))

        if not stones:
            return 0
        return -stones[0]
