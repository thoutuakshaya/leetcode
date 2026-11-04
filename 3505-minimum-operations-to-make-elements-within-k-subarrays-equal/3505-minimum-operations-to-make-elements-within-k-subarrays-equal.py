

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # Coordinate compression
        values = sorted(set(nums))
        m = len(values)

        def get_index(v):
            import bisect
            return bisect.bisect_left(values, v) + 1

        # Fenwick Tree
        class BIT:
            def __init__(self, n):
                self.n = n
                self.tree = [0] * (n + 1)

            def add(self, i, val):
                while i <= self.n:
                    self.tree[i] += val
                    i += i & -i

            def query(self, i):
                result = 0
                while i > 0:
                    result += self.tree[i]
                    i -= i & -i
                return result

            def kth(self, target):
                idx = 0
                bit = 1 << (self.n.bit_length() - 1)

                while bit:
                    nxt = idx + bit
                    if nxt <= self.n and self.tree[nxt] < target:
                        target -= self.tree[nxt]
                        idx = nxt
                    bit >>= 1

                return idx + 1

        freq = BIT(m)
        sums = BIT(m)

        # Initialize first window
        for v in nums[:x]:
            idx = get_index(v)
            freq.add(idx, 1)
            sums.add(idx, v)

        costs = [0] * (n - x + 1)

        total = sum(nums[:x])

        # Calculate cost of every sliding window
        for start in range(n - x + 1):

            # Find median
            mid_idx = freq.kth((x + 1) // 2)
            median = values[mid_idx - 1]

            # Values <= median
            left_count = freq.query(mid_idx)
            left_sum = sums.query(mid_idx)

            right_count = x - left_count
            right_sum = total - left_sum

            # Minimum operations
            costs[start] = (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

            # Slide window
            if start + x < n:
                old = nums[start]
                new = nums[start + x]

                old_idx = get_index(old)
                new_idx = get_index(new)

                freq.add(old_idx, -1)
                sums.add(old_idx, -old)

                freq.add(new_idx, 1)
                sums.add(new_idx, new)

                total += new - old

        # DP: minimum cost for selecting exactly j windows
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # Skip current element
                curr[i] = curr[i - 1]

                # Select window ending at i - 1
                if i >= x:
                    candidate = prev[i - x] + costs[i - x]
                    curr[i] = min(curr[i], candidate)

            prev = curr

        return prev[n]
