class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        lengths = [0] * (n + 1)

        for i, ch in enumerate(s):
            curr = lengths[i]

            if ch.isalpha():
                lengths[i + 1] = curr + 1

            elif ch == '*':
                lengths[i + 1] = max(0, curr - 1)

            elif ch == '#':
                lengths[i + 1] = curr * 2

            else:  # '%'
                lengths[i + 1] = curr

        if k >= lengths[n]:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]
            prev_len = lengths[i]
            curr_len = lengths[i + 1]

            if ch.isalpha():
                if k == prev_len:
                    return ch

            elif ch == '*':
                pass

            elif ch == '#':
                k %= prev_len

            else:  # '%'
                k = curr_len - 1 - k

        return '.'