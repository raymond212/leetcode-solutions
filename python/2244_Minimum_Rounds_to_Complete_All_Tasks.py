class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = Counter(tasks).values()
        ans = 0
        for count in freq:
            if count == 1:
                return -1
            # If count % 3 == 0: (count // 3) triples and 0 pairs 
            # If count % 3 == 1: (count // 3 - 1) triples and 2 pairs
            # If count % 3 == 2: (count // 3) triples and 1 pair
            ans += (count + 2) // 3
        return ans