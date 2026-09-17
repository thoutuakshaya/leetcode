class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        INF = float('inf')
        dp = [INF] * (n + 1)

        ans = INF
        left = 0
        curr_sum = 0
        best = INF

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # Previous subarray must end before 'left'
                if dp[left] != INF:
                    ans = min(ans, dp[left] + length)

                best = min(best, length)

            dp[right + 1] = best

        return -1 if ans == INF else ans