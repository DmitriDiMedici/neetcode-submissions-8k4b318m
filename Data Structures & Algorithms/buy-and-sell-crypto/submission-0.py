class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        max_profit = 0

        for right in range(1, len(prices)):
            if prices[right] > prices[left]:
                todays_earnings = prices[right] - prices[left]
                if todays_earnings > max_profit:
                    max_profit = todays_earnings
            else:
                left = right

        return max_profit