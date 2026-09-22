class Solution:
    def resultArray(self, nums, k, queries):

        n = len(nums)

        # Each node:
        # [product_of_whole_segment % k, prefix_counts]
        tree = [[0, [0] * k] for _ in range(4 * n)]

        def merge(left, right):
            left_prod, left_pref = left
            right_prod, right_pref = right

            prod = (left_prod * right_prod) % k
            pref = left_pref[:]

            # Prefix = entire LEFT + prefix of RIGHT
            for r in range(k):
                new_r = (left_prod * r) % k
                pref[new_r] += right_pref[r]

            return [prod, pref]

        def build(node, l, r):
            if l == r:
                rem = nums[l] % k
                tree[node] = [rem, [0] * k]
                tree[node][1][rem] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, value):
            if l == r:
                rem = value % k
                tree[node] = [rem, [0] * k]
                tree[node][1][rem] = 1
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            # Completely inside range
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            # Entirely in right
            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            # Entirely in left
            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            # Split between left and right
            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        result = []

        for index, value, start, x in queries:

            # Update persists for future queries
            update(1, 0, n - 1, index, value)

            # We need all prefixes starting from 'start'
            node = query(1, 0, n - 1, start, n - 1)

            result.append(node[1][x])

        return result