from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:

        count = Counter(s)
        n = len(s)

        # Check whether a palindromic permutation is possible
        odd = []

        for c in count:
            if count[c] % 2 == 1:
                odd.append(c)

        if len(odd) > 1:
            return ""

        middle = odd[0] if odd else ""

        # Frequency of characters needed for LEFT HALF
        freq = [0] * 26

        for c, cnt in count.items():
            freq[ord(c) - ord('a')] = cnt // 2

        m = n // 2

        # -------------------------------------------------
        # Try to match target's left half
        # -------------------------------------------------

        prefix = []

        i = 0

        while i < m:
            idx = ord(target[i]) - ord('a')

            if freq[idx] == 0:
                break

            prefix.append(target[i])
            freq[idx] -= 1
            i += 1

        # -------------------------------------------------
        # If complete left half matched,
        # check the resulting palindrome directly
        # -------------------------------------------------

        if i == m:
            left = ''.join(prefix)
            candidate = left + middle + left[::-1]

            if candidate > target:
                return candidate

        # -------------------------------------------------
        # Backtrack
        # At each position, try the smallest character
        # greater than target[i]
        # -------------------------------------------------

        for pos in range(i, -1, -1):

            # Restore character at this position
            # because we are going backward
            if pos < len(prefix):
                removed = prefix.pop()
                freq[ord(removed) - ord('a')] += 1

            # If pos == m, there is no position to increase
            if pos >= m:
                continue

            target_idx = ord(target[pos]) - ord('a')

            # Find smallest available character > target[pos]
            for j in range(target_idx + 1, 26):

                if freq[j] > 0:

                    # Use this larger character
                    freq[j] -= 1

                    result = prefix[:] + [chr(ord('a') + j)]

                    # Add remaining characters in smallest order
                    for k in range(26):
                        result.extend(
                            [chr(ord('a') + k)] * freq[k]
                        )

                    left = ''.join(result)

                    return left + middle + left[::-1]

        return ""