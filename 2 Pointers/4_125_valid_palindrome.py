class Solution:
  def isPalindrome(self, s: str) -> bool:
    left_index = 0
    right_index = len(s) - 1
    while left_index < right_index: 
      if s[left_index].isalnum() == False: 
        left_index += 1
      elif s[right_index].isalnum() == False: 
        right_index -= 1
      else: 
        if s[left_index].lower() != s[right_index].lower(): 
          return False
        left_index += 1
        right_index -= 1
    return True

    # for letter in s:
    #   if letter.isalnum() == False:
    #     s = s.replace(letter, "")
    #   elif letter.isupper():
    #     s = s.replace(letter, letter.lower())
    # holder = list(s)
    # left_index, right_index = 0, len(s) - 1
    # for i in range(len(s) // 2):
    #   holder[left_index], holder[right_index] = holder[right_index], holder[left_index]
    #   left_index += 1
    #   right_index -= 1
    # # print(f"{holder}\n{list(s)}")
    # if holder == list(s):
    #   return True
    # return False

solution = Solution()
s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s))

## Final Draft
## Run Time: 44ms (Beats 62.48%) 
## Memory: 17.01mb (Beats 54.72%)
## Time Complexity: O(n)

## First Draft
## Run Time: 1463ms (Beats 5.19%) 
## Memory: 17.80mb (Beats 31.74%)
## Time Complexity: O(n^2)