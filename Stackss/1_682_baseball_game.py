class Solution:
  def calPoints(self, operations: list[str]) -> int:
    score_tally = []
    for element in operations: 
      if element.isdigit() or element[0] == "-":
        score_tally.append(int(element))
      elif element == "C":
        score_tally.pop()
      elif element == "D":
        score_tally.append(score_tally[-1]*2)
      elif element == "+":
        score_tally.append(score_tally[-1]+score_tally[-2])
      # print(score_tally)
    # print(score_tally)
    return sum(score_tally)
  
operations = ["1","C"]
solution = Solution()
print(solution.calPoints(operations))

## Run Time: 40ms (Beats 79.02%) 
## Memory: 16.79mb (Beats 42.02%)
## Time Complexity: O(n)
## Space Complexity: O(n)