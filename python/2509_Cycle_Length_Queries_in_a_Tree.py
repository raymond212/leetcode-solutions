class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        answer = []
        for x, y in queries:
            length = 1
            while x != y:
                if x > y:
                    x //= 2
                else:
                    y //= 2
                length += 1
            answer.append(length)
        return answer
        