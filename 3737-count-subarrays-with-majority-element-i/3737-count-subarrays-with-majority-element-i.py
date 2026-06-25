from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        pref = [0]
        cur = 0

        for x in nums:
            cur += 1 if x == target else -1
            pref.append(cur)

        vals = sorted(set(pref))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        m = len(vals)
        bit = [0] * (m + 1)

        def update(i, delta):
            while i <= m:
                bit[i] += delta
                i += i & -i

        def query(i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s

        ans = 0

        for p in pref:
            r = rank[p]

            # count previous prefix sums smaller than p
            ans += query(r - 1)

            update(r, 1)

        return ans