from math import ceil, floor
class Solution:
  def evalRPN(self, tokens: list[str]) -> int:
    if len(tokens) == 1 and tokens[0].isdigit():
      return int(tokens[0])
    stack = []
    for element in tokens:
      if element in "+-/*":
        number1, number2 = stack.pop(), stack.pop()
        if element == "+": 
          stack.append(number1 + number2)
        elif element == "-":
          stack.append(number2 - number1)
        elif element == "*":
          stack.append(number1 * number2)
        elif element == "/": 
          if number2 == 0: 
            stack.append(0)
          else:
            if number2 / number1 < 0: 
              stack.append(ceil(number2 / number1))
            else: 
              stack.append(floor(number2 / number1))
      else: 
        stack.append(int(element))
    return stack[0]
  
tokens =["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
solution = Solution() 
print(solution.evalRPN(tokens))

## Run Time: 61ms (Beats 81.65%) 
## Memory: 17.12mb (Beats 13.56%)
## Time Complexity: O(n)
## Space Complexity: O(n)