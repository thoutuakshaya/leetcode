class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):

        rows = {}

        # Store reserved seats for each affected row
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()

            rows[row].add(seat)

        # Rows with no reservations can always fit 2 groups
        answer = (n - len(rows)) * 2

        # Check only rows that have reservations
        for seats in rows.values():

            left = all(seat not in seats for seat in [2, 3, 4, 5])
            middle = all(seat not in seats for seat in [4, 5, 6, 7])
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            if left and right:
                answer += 2

            elif left or right or middle:
                answer += 1

        return answer