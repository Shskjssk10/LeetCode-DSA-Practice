class Solution:
  def maxArea(self, height: list[int]) -> int:
    if len(height) == 2:
      return 1 * min(height)
    left_index = 0
    right_index = len(height) - 1
    max = float('-inf')
    while left_index < right_index: 
      current_area = (right_index - left_index) * min(height[left_index], height[right_index])
      if current_area > max: 
        max = current_area
      if height[right_index] > height[left_index]:
        left_index += 1
      else: 
        right_index -= 1
    return max
  
solution = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(height))

## Run Time: 500ms (Beats 85.22%) 
## Memory: 29.47mb (Beats 65.83%)
## Time Complexity: O(n)
