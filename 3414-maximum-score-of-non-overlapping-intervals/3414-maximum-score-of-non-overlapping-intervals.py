from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        n = len(intervals)

        # l, r, weight, original index
        arr = [
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        ]

        # Sort by starting point
        arr.sort()

        starts = [x[0] for x in arr]

        # nxt[i] = first interval whose start > arr[i].right
        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        # dp[i][k] = (maximum score, lexicographically smallest indices)
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):

            l, r, w, idx = arr[i]

            for k in range(1, 5):

                # Option 1: skip current interval
                skip = dp[i + 1][k]

                # Option 2: take current interval
                next_score, next_indices = dp[nxt[i]][k - 1]

                take_indices = tuple(sorted(next_indices + (idx,)))

                take = (
                    w + next_score,
                    take_indices
                )

                # Higher score is better
                if take[0] > skip[0]:
                    dp[i][k] = take

                # Same score -> lexicographically smaller indices
                elif take[0] == skip[0]:
                    dp[i][k] = min(take, skip)

                else:
                    dp[i][k] = skip

        return list(dp[0][4][1])