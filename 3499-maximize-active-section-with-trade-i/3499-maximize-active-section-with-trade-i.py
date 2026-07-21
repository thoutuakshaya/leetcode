class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ans = 0
        pre = float("-inf")
        mx = 0

        i = 0
        n = len(s)

        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1

            length = j - i

            if s[i] == '1':
                ans += length
            else:
                mx = max(mx, pre + length)
                pre = length

            i = j

        return ans + mx