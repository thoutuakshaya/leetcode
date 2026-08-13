class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:

        n = len(s)

        # Segment tree node:
        # [left_char, right_char, prefix, suffix, best, length]
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            left_char = a[0]
            right_char = b[1]

            prefix = a[2]
            suffix = b[3]

            # If the entire left segment has the same character
            if a[2] == a[5] and a[1] == b[0]:
                prefix += b[2]

            # If the entire right segment has the same character
            if b[3] == b[5] and a[1] == b[0]:
                suffix += a[3]

            best = max(a[4], b[4])

            # Join suffix of left + prefix of right
            if a[1] == b[0]:
                best = max(best, a[3] + b[2])

            return (
                left_char,
                right_char,
                prefix,
                suffix,
                best,
                a[5] + b[5]
            )

        def build(node, l, r):
            if l == r:
                tree[node] = (s[l], s[l], 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, char):
            if l == r:
                tree[node] = (char, char, 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, r, index, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)
            ans.append(tree[1][4])

        return ans