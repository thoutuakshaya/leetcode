import bisect
from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')

        # Run-length encode s into (char, start, end)
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], i, j - 1))
            i = j
        R = len(runs)

        run_start = [r[1] for r in runs]
        length = [r[2] - r[1] + 1 for r in runs]
        chars = [r[0] for r in runs]

        def run_index(pos: int) -> int:
            return bisect.bisect_right(run_start, pos) - 1

        NEG = -1
        g = [NEG] * R
        for k in range(1, R - 1):
            if chars[k] == '1':
                g[k] = length[k - 1] + length[k + 1]

        # Sparse table for range-max over g
        LOG = [0] * (R + 2)
        for i in range(2, R + 2):
            LOG[i] = LOG[i // 2] + 1

        st = [g[:]] if R > 0 else [[]]
        j = 1
        while (1 << j) <= R:
            prev = st[-1]
            half = 1 << (j - 1)
            cur = [max(prev[i], prev[i + half]) for i in range(R - (1 << j) + 1)]
            st.append(cur)
            j += 1

        def query_max(l: int, r: int) -> int:
            if l > r:
                return NEG
            k = LOG[r - l + 1]
            return max(st[k][l], st[k][r - (1 << k) + 1])

        ans = []
        for l, r in queries:
            kl = run_index(l)
            kr = run_index(r)
            best = 0
            if kr - kl >= 2:
                for k in {kl + 1, kr - 1}:
                    if chars[k] == '1':
                        left_len = runs[k - 1][2] - max(runs[k - 1][1], l) + 1
                        right_len = min(runs[k + 1][2], r) - runs[k + 1][1] + 1
                        gain = left_len + right_len
                        if gain > best:
                            best = gain
                if kr - kl >= 4:
                    m = query_max(kl + 2, kr - 2)
                    if m > best:
                        best = m
            ans.append(total_ones + best)

        return ans