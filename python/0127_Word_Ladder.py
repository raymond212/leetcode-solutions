class Solution:
    def ladderLength(self, start: str, end: str, dictionary: List[str]) -> int:
        dict = set(dictionary)
        visited = {start}
        queue = collections.deque([start])
        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return steps
                for next_word in self.next_words(word):
                    if next_word in dict and next_word not in visited:
                        queue.append(next_word)
                        visited.add(next_word)

        return 0

    def next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in "abcdefghijklmnopqrstuvwxyz":
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words