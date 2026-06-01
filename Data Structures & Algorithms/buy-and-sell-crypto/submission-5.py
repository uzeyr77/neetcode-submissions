class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       left = 0
       right = 1
       max_profit = 0
       profit = 0
       if len(prices) <= 1:
        return 0

       while(right < len(prices)):
        if prices[left] < prices[right]: # is it profitable
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
        else:
            left = right
        right += 1

       return max_profit