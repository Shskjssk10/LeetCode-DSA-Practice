class Solution:
  def isPalindrome(self, s: str) -> bool:
    holder = list(s)
    left_index = 0
    right_index = len(s) - 1
    while left_index < right_index:
      if holder[left_index].isalnum() is False:
        s = s.replace(holder[left_index], "")
        del holder[left_index]
        left_index += 1
      elif holder[right_index].isalnum() is False: 
        s = s.replace(holder[right_index], "")
        del holder[right_index]
        right_index -= 1
      else:
        holder[left_index], holder[right_index] = holder[right_index].lower(), holder[left_index].lower()
        left_index += 1
        right_index -= 1
    print(f"{holder}\n{list(s.lower())}")
    if list(s.lower()) == holder:
      return True
    return False

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

## First Draft
## Run Time: 1463ms (Beats 5.19%) 
## Memory: 17.80mb (Beats 31.74%)
## Time Complexity: O(n^2)