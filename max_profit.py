class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_val = float('inf')
        profit = 0
        
        for price in prices:
            if price < buy_val:
                buy_val = price
                
            curr_price = price - buy_val
            
            if curr_price > profit:
                profit = curr_price
                
        return profit