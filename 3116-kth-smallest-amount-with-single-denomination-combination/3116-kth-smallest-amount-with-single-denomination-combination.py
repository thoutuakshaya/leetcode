
from typing import List
from math import gcd
from itertools import combinations


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Remove redundant coins.
        # If a coin is a multiple of a smaller coin, its multiples
        # are already covered by the smaller coin.
        coins.sort()
        filtered = []

        for coin in coins:
            if not any(coin % prev == 0 for prev in filtered):
                filtered.append(coin)

        coins = filtered
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        # Count how many DISTINCT amounts <= x can be formed.
        # Inclusion-Exclusion:
        # multiples of a OR multiples of b OR ...
        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                curr_lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        curr_lcm = lcm(curr_lcm, coins[i])

                        # LCM already too large, contributes 0
                        if curr_lcm > x:
                            break

                else:
                    if bits % 2 == 1:
                        total += x // curr_lcm
                    else:
                        total -= x // curr_lcm

            return total

        # kth answer is at most min(coins) * k
        left, right = 1, min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left