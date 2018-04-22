"""
You are given a list of prices for a certain stock throughout the day. What's
the maximum profit you can make off one trade (buy one share and sell one
share)? You must buy the stock before you sell it. If there is no profit to be
made, return 0.

Example:
[3, 7, 1, 6, 4] -> 5
[5, 4, 3, 2, 1] -> 0
"""

def get_max_profit(prices):
    # max_profit = 0
    # for a in range(len(prices)):
    #     for b in range(a, len(prices)):
    #         if prices[b] - prices[a] > max_profit:
    #             max_profit = prices[b] - prices[a]
    # return max_profit
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price - min_price > max_profit:
            max_profit = price - min_price
        if price < min_price:
            min_price = price
    return max_profit

print(get_max_profit([3, 7, 1, 6, 4]))
print(get_max_profit([5, 4, 3, 2, 1]))
