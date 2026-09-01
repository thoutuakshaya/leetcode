
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])

        removed = 0
        end = intervals[0][1]

        for i in range(1, len(intervals)):

            if intervals[i][0] < end:
                removed += 1
            else:
                end = intervals[i][1]

        return removed