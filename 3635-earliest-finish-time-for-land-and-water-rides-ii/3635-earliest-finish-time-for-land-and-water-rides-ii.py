from typing import List
from bisect import bisect_right

class Solution:

    def solve(self, firstStart, firstDuration,
                    secondStart, secondDuration):

        # Step 1: Create (start, duration) pairs
        rides = []

        for i in range(len(secondStart)):
            rides.append((secondStart[i], secondDuration[i]))

        # Sort by start time
        rides.sort()

        # Step 2: Extract start times
        starts = []

        for ride in rides:
            starts.append(ride[0])

        n = len(rides)

        # Step 3: Prefix minimum duration
        prefixMinDur = [0] * n

        prefixMinDur[0] = rides[0][1]

        for i in range(1, n):
            prefixMinDur[i] = min(
                prefixMinDur[i - 1],
                rides[i][1]
            )

        # Step 4: Suffix minimum (start + duration)
        suffixMinFinish = [0] * n

        suffixMinFinish[n - 1] = (
            rides[n - 1][0] +
            rides[n - 1][1]
        )

        for i in range(n - 2, -1, -1):

            currentFinish = (
                rides[i][0] +
                rides[i][1]
            )

            suffixMinFinish[i] = min(
                suffixMinFinish[i + 1],
                currentFinish
            )

        answer = float('inf')

        # Step 5: Process every ride of first type
        for i in range(len(firstStart)):

            finishTime = (
                firstStart[i] +
                firstDuration[i]
            )

            # Find last ride with start <= finishTime
            index = bisect_right(
                starts,
                finishTime
            ) - 1

            # Case 1:
            # second ride already available
            if index >= 0:

                candidate = (
                    finishTime +
                    prefixMinDur[index]
                )

                answer = min(
                    answer,
                    candidate
                )

            # Case 2:
            # second ride starts later
            if index + 1 < n:

                candidate = (
                    suffixMinFinish[index + 1]
                )

                answer = min(
                    answer,
                    candidate
                )

        return answer

    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        landFirst = self.solve(
            landStartTime,
            landDuration,
            waterStartTime,
            waterDuration
        )

        waterFirst = self.solve(
            waterStartTime,
            waterDuration,
            landStartTime,
            landDuration
        )

        return min(
            landFirst,
            waterFirst
        )