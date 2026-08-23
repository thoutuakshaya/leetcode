class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2

        leftSum = 0
        rightSum = 0
        leftQ = 0
        rightQ = 0

        # Left half
        for i in range(mid):
            if num[i] == '?':
                leftQ += 1
            else:
                leftSum += int(num[i])

        # Right half
        for i in range(mid, n):
            if num[i] == '?':
                rightQ += 1
            else:
                rightSum += int(num[i])

        # Alice gets an extra move
        if (leftQ + rightQ) % 2 == 1:
            return True

        # Bob wins only in this exact balanced situation
        return 2 * (leftSum - rightSum) != 9 * (rightQ - leftQ)