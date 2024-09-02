class Solution:
  def isValid(self, s: str) -> bool:
    if len(s) < 2: 
      return False
    stack = []
    dictionary = { ")" : "(", "]" : "[", "}" : "{"}
    for charcater in s: 
      if charcater not in dictionary: 
        stack.append(charcater)
      else: 
        if dictionary[charcater] not in stack or stack[-1] != dictionary[charcater]:
          return False
        elif stack[-1] == dictionary[charcater]: 
          stack.pop()
    if len(stack) == 0:
      return True
    return False

  
s = "(("
solution = Solution()
print(solution.isValid(s))

## Run Time: 30ms (Beats 87.51%) 
## Memory: 16.45mb (Beats 90.51%)
## Time Complexity: O(n)
## Space Complexity: O(n)