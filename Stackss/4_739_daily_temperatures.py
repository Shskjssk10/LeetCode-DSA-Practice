from collections import deque

class Solution:
  def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    most_warm = temperatures[-1]
    answer = [0]
    if len(temperatures) == 1:
      return answer
    for i in range(len(temperatures - 1)):
      number = temperatures.pop()
      if number > most_warm:
        most_warm = number
      
    
    


  
temperatures = [73,74,75,71,69,72,76,73]
solution = Solution()
print(solution.dailyTemperatures(temperatures))