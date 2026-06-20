class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:

        restrictions.append([1, 0])

        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])

        restrictions.sort()

        m = len(restrictions)

        # Left to right
        for i in range(1, m):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] +
                (restrictions[i][0] - restrictions[i - 1][0])
            )

        # Right to left
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] +
                (restrictions[i + 1][0] - restrictions[i][0])
            )

        ans = 0

        for i in range(1, m):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            d = x2 - x1

            peak = (h1 + h2 + d) // 2

            ans = max(ans, peak)

        return ans