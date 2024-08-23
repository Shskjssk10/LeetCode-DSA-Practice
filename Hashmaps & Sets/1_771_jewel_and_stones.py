class Solution:
  def numJewelsInStones(jewels, stones) -> int:
    jewels = set(jewels)
    count = 0
    for stone in stones:
      if stone in jewels:
        count += 1
    return count
  
  jewels = "aA"
  stones = "aAAbbbb"
  print(numJewelsInStones(jewels, stones))

  ## Run Time: 22ms (Beats 99.34%) 
  ## Memory: 16.50mb (Beats 67.36%)