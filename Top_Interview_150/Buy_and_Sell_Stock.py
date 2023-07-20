class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        minimum = prices[0]
        max_profit = 0
        index = 0
        for i in range (len(prices)):
            if minimum > prices[i]:
                minimum = prices[i]
                index = i

        Buying_Price = prices[index]

        for i in range(index,len(prices)):
            currentProfit = prices[i] - Buying_Price
            if index < len(prices):
                max_profit =max(currentProfit,max_profit)
            
        return max_profit
            



if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1,2]))