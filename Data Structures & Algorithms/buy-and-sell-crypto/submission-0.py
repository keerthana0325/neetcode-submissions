class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<mini:
                mini = prices[i]
            else:
                pro = prices[i] - mini 
                if pro > profit :
                    profit = pro 
        return profit
        