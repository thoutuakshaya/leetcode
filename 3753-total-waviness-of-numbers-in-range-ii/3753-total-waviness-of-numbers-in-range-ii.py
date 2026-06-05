from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n):
            if n < 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            @lru_cache(None)
            def dp(pos, tight, started, prev1, prev2):
                """
                Returns:
                (count_numbers, total_waviness)
                """

                if pos == m:
                    return (1, 0)

                limit = digits[pos] if tight else 9

                total_count = 0
                total_wave = 0

                for d in range(limit + 1):

                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            False,
                            -1,
                            -1
                        )

                        total_count += cnt
                        total_wave += wav

                    else:
                        if not started:
                            cnt, wav = dp(
                                pos + 1,
                                ntight,
                                True,
                                d,
                                -1
                            )

                            total_count += cnt
                            total_wave += wav

                        else:
                            add = 0

                            if prev2 != -1:
                                if ((prev1 > prev2 and prev1 > d) or
                                    (prev1 < prev2 and prev1 < d)):
                                    add = 1

                            cnt, wav = dp(
                                pos + 1,
                                ntight,
                                True,
                                d,
                                prev1
                            )

                            total_count += cnt
                            total_wave += wav + add * cnt

                return (total_count, total_wave)

            return dp(0, True, False, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)