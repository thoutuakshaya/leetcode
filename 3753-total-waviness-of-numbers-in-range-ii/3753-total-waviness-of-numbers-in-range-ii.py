from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        # Returns total waviness of all numbers from 0 to n
        def get_total_waviness_upto(n):

            if n < 0:
                return 0

            digits = list(map(int, str(n)))
            length = len(digits)

            @lru_cache(None)
            def dp(position, tight, started, previous_digit, second_previous_digit):

                # Reached end of number
                if position == length:
                    return (1, 0)  # (count_of_numbers, total_waviness)

                limit = digits[position] if tight else 9

                total_numbers = 0
                total_waviness = 0

                for current_digit in range(limit + 1):

                    new_tight = tight and (current_digit == limit)

                    # Still skipping leading zeros
                    if not started and current_digit == 0:

                        count, waviness = dp(
                            position + 1,
                            new_tight,
                            False,
                            -1,
                            -1
                        )

                        total_numbers += count
                        total_waviness += waviness

                    else:

                        # First actual digit
                        if not started:

                            count, waviness = dp(
                                position + 1,
                                new_tight,
                                True,
                                current_digit,
                                -1
                            )

                            total_numbers += count
                            total_waviness += waviness

                        else:

                            new_peak_or_valley = 0

                            # We have 3 digits:
                            # second_previous_digit, previous_digit, current_digit
                            if second_previous_digit != -1:

                                is_peak = (
                                    previous_digit > second_previous_digit
                                    and previous_digit > current_digit
                                )

                                is_valley = (
                                    previous_digit < second_previous_digit
                                    and previous_digit < current_digit
                                )

                                if is_peak or is_valley:
                                    new_peak_or_valley = 1

                            count, waviness = dp(
                                position + 1,
                                new_tight,
                                True,
                                current_digit,
                                previous_digit
                            )

                            total_numbers += count

                            total_waviness += (
                                waviness
                                + new_peak_or_valley * count
                            )

                return (total_numbers, total_waviness)

            return dp(0, True, False, -1, -1)[1]

        return (
            get_total_waviness_upto(num2)
            - get_total_waviness_upto(num1 - 1)
        )