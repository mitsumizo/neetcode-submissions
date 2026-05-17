class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_range = 0
        buy_min_value = prices[0]

        for index in range(1, len(prices)):
            max_range = max(prices[index] - buy_min_value, max_range)
            buy_min_value = min(buy_min_value, prices[index])
        return max_range   
