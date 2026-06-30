class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force Approach
        # profit = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i+1, len(prices)):
        #         sell = prices[j]
        #         profit = max(profit, sell - buy)
        # return profit
        
        # Sliding Window Approach
        profit = 0
        buy, sell = 0, 1
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell
            
            sell += 1
        
        return profit