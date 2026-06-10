import heapq

class Solution(object):
    def maxTotalValue(self, nums, k):
        n = len(nums)

        # Sparse tables
        LOG = (n).bit_length()

        st_max = [[0] * n for _ in range(LOG)]
        st_min = [[0] * n for _ in range(LOG)]

        for i in range(n):
            st_max[0][i] = nums[i]
            st_min[0][i] = nums[i]

        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1

            for i in range(n - length + 1):
                st_max[j][i] = max(
                    st_max[j - 1][i],
                    st_max[j - 1][i + half]
                )

                st_min[j][i] = min(
                    st_min[j - 1][i],
                    st_min[j - 1][i + half]
                )

            j += 1

        log = [0] * (n + 1)
        for i in range(2, n + 1):
            log[i] = log[i // 2] + 1

        def value(l, r):
            length = r - l + 1
            p = log[length]

            mx = max(
                st_max[p][l],
                st_max[p][r - (1 << p) + 1]
            )

            mn = min(
                st_min[p][l],
                st_min[p][r - (1 << p) + 1]
            )

            return mx - mn

        heap = []

        for l in range(n):
            v = value(l, n - 1)
            heapq.heappush(heap, (-v, l, n - 1))

        ans = 0

        for _ in range(k):
            neg_v, l, r = heapq.heappop(heap)

            ans += -neg_v

            if r > l:
                nv = value(l, r - 1)
                heapq.heappush(heap, (-nv, l, r - 1))

        return ans