class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        idx = 0
        while idx < len(words):
            arr = []
            num_words = 0
            line_length = 0
            while idx < len(words) and (line_length + len(words[idx]) + num_words) <= maxWidth:
                arr.append(words[idx])
                num_words += 1
                line_length += len(words[idx])
                idx += 1
            total_space = maxWidth - line_length
            if num_words == 1:
                res.append(arr[0] + ' ' * total_space)
                continue
            if idx == len(words):
                line = ' '.join(arr)
                line += ' ' * (maxWidth - len(line))
                res.append(line)
            else:
                base_space = total_space // (num_words - 1)
                num_extra = total_space % (num_words - 1)
                line = ''
                for i in range(len(arr) - 1):
                    line += arr[i]
                    num_space = base_space + (1 if i < num_extra else 0)
                    line += ' ' * num_space
                line += arr[-1]
                res.append(line)
        return res