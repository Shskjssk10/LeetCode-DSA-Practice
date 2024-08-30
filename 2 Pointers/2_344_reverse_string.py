class Solution:
  def reverseString(self, s: list[str]) -> None:  
    left_index = 0
    right_index = len(s) - 1
    for i in range(len(s) // 2):
      s[left_index], s[right_index] = s[right_index], s[left_index]
      left_index += 1
      right_index -= 1

solution = Solution()
s = ["h","e","l","l","o"]
solution.reverseString(s)

## Run Time: 161ms (Beats 89.50%) 
## Memory: 10.79mb (Beats 87.78%)