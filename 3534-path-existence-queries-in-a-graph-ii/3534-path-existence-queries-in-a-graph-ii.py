from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((v, i) for i, v in enumerate(nums))

        pos = [0] * n
        comp = [0] * n

        m = len(arr)

        nxt = [0] * m

        j = 0
        cid = 0

        for i in range(m):
            while j + 1 < m and arr[j + 1][0] - arr[i][0] <= maxDiff:
                j += 1

            nxt[i] = j

            if i > 0 and arr[i][0] - arr[i - 1][0] > maxDiff:
                cid += 1

            comp[arr[i][1]] = cid
            pos[arr[i][1]] = i

        LOG = 18
        up = [[0] * m for _ in range(LOG)]

        for i in range(m):
            up[0][i] = nxt[i]

        for k in range(1, LOG):
            for i in range(m):
                up[k][i] = up[k - 1][up[k - 1][i]]

        ans = []

        for u, v in queries:

            if u == v:
                ans.append(0)
                continue

            if comp[u] != comp[v]:
                ans.append(-1)
                continue

            l = pos[u]
            r = pos[v]

            if l > r:
                l, r = r, l

            cur = l
            res = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < r:
                    cur = up[k][cur]
                    res += 1 << k

            ans.append(res + 1)

        return ans