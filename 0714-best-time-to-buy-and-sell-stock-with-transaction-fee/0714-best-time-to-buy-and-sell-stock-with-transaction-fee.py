class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        hold = -prices[0]
        cash = 0

        for price in prices:

            old_hold = hold
            old_cash = cash

            cash = max(old_cash, old_hold + price - fee)

            hold = max(old_hold, old_cash - price)

        return cash