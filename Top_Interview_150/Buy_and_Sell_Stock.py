class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy_price = 0
        sell_price = 1
        while(sell_price < len(prices)):
            current_profit = prices[sell_price]-prices[buy_price]
            if(prices[buy_price]< prices[sell_price]):
                max_profit = max(current_profit,max_profit)
            else :
                buy_price = sell_price
            sell_price = sell_price + 1
           
        # print(buy_price)
        return max_profit




if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([2,4,1]))