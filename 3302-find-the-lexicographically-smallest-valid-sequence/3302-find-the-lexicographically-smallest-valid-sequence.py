class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        # right[j] = position used for word2[j]
        # when matching word2[j:] from right to left
        right = [-1] * m

        i = n - 1

        for j in range(m - 1, -1, -1):
            while i >= 0 and word1[i] != word2[j]:
                i -= 1

            if i < 0:
                break

            right[j] = i
            i -= 1

        ans = []
        j = 0
        mismatch = 0

        for i in range(n):

            if j == m:
                break

            # Case 1: exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Case 2: use our one mismatch
            elif mismatch == 0:
                # Nothing remains after this character
                if j == m - 1:
                    ans.append(i)
                    mismatch = 1
                    j += 1

                # Remaining suffix must be exactly matchable
                elif right[j + 1] != -1 and right[j + 1] > i:
                    ans.append(i)
                    mismatch = 1
                    j += 1

        if j == m:
            return ans

        return []