from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
       
        count = Counter(s)
        n = len(s)

        # prefix[i] = characters used to match target[0:i]
        prefix = []

        for i in range(n):
            if count[target[i]] > 0:
                prefix.append(target[i])
                count[target[i]] -= 1
            else:
                break

        # Try from right to left
        for i in range(len(prefix), -1, -1):

            # Restore character at position i if we are moving back
            if i < len(prefix):
                count[prefix[i]] += 1

            # Find smallest character greater than target[i]
            if i < n:
                for c in range(ord(target[i]) + 1, ord('z') + 1):
                    char = chr(c)

                    if count[char] > 0:
                        count[char] -= 1

                        # Prefix + greater character
                        answer = prefix[:i] + [char]

                        # Add remaining characters in sorted order
                        for j in range(26):
                            answer.extend(
                                chr(ord('a') + j) * count[chr(ord('a') + j)]
                            )

                        return "".join(answer)

        return ""