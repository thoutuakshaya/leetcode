

        
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:

        first = {}
        last = {}

        # Find first and last occurrence
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []

        # Build valid intervals
        for ch in first:
            left = first[ch]
            right = last[ch]

            i = left
            valid = True

            while i <= right:
                c = s[i]

                # This character appeared before our interval
                if first[c] < left:
                    valid = False
                    break

                right = max(right, last[c])
                i += 1

            if valid:
                intervals.append((left, right))

        # Greedily choose non-overlapping intervals
        intervals.sort(key=lambda x: x[1])

        result = []
        end = -1

        for left, right in intervals:
            if left > end:
                result.append(s[left:right + 1])
                end = right

        return result