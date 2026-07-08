from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        vals = []
        pos = []

        for i, ch in enumerate(s):
            if ch != '0':
                vals.append(int(ch))
                pos.append(i)

        m = len(vals)

        # powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix concatenated value
        pref = [0] * (m + 1)
        for i in range(m):
            pref[i + 1] = (pref[i] * 10 + vals[i]) % MOD

        # prefix digit sums
        digit_sum = [0] * (m + 1)
        for i in range(m):
            digit_sum[i + 1] = digit_sum[i] + vals[i]

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            x = (
                pref[right + 1]
                - pref[left] * pow10[length]
            ) % MOD

            ssum = digit_sum[right + 1] - digit_sum[left]

            ans.append((x * ssum) % MOD)

        return ans