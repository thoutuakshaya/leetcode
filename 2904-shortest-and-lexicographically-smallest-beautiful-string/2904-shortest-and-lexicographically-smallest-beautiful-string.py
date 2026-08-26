class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""

        for left in range(len(s)):
            count = 0

            for right in range(left, len(s)):
                if s[right] == '1':
                    count += 1

                if count == k:
                    current = s[left:right + 1]

                    if ans == "" or len(current) < len(ans):
                        ans = current
                    elif len(current) == len(ans) and current < ans:
                        ans = current

                    break

        return ans