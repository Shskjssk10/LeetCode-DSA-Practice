class Solution:
  def maxProfit(prices) -> int:
    smallest_price = float('inf')
    max_profit = 0

    for price in prices:
      if price < smallest_price:
        smallest_price = price
      if max_profit < price - smallest_price:
        max_profit = price - smallest_price
    if max_profit < 0:
      return 0
    return max_profit

  prices = [7,6,4,3,1]
  print(maxProfit(prices))

  ## Run Time: 681ms (Beats 90.38%) 
  ## Memory: 27.38mb (Beats 82.01%)
