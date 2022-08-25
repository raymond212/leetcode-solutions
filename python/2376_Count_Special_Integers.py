class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        str_n = str(n)
        digit_count = len(str_n)
        res = 0
        for i in range(1, digit_count):
            count = 9
            for j in range(1, i):
                count *= (10 - j)
            res += count

        digit_repeat = False
        seen = set()
        for i in range(digit_count):
            if digit_repeat:
                continue
            digit = int(str_n[i])
            if i < digit_count - 1 and digit in seen:
                digit_repeat = True
            num_smaller = digit
            if i == digit_count - 1:
                if i == 0:
                    res += digit
                    break
                for j in range(0, digit + 1):
                    if j in seen:
                        continue
                    res += 1
                break

            for j in range(num_smaller):
                if i == 0 and j == 0:
                    continue
                if j in seen:
                    continue
                options = 9 - len(seen)
                res += self.distinct_n_digit(digit_count - i - 1, options)
            seen.add(digit)
            
        return res

    def distinct_n_digit(self, n, options):
        count = 1
        for j in range(n):
            count *= (options - j)
        return count
        