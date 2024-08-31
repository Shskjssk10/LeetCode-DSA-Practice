class Solution:
  def threeSum(self, nums: list[int]) -> list[list[int]]:
    if len(nums) == 3 and sum(nums) == 0: 
      return [nums]
    elif len(nums) == 3 and sum(nums) != 0:
      return []
    nums.sort()
    answer = list()
    for i in range(len(nums)-2):
      number = nums[i]
      left_index = i + 1
      right_index = len(nums) - 1
      if number == nums[i-1] and i > 0: 
        continue
      while left_index < right_index:
        current_sum = number + nums[left_index] + nums[right_index]

        if current_sum == 0:
          answer.append([number, nums[left_index], nums[right_index]])
          while left_index < right_index and nums[left_index] == nums[left_index + 1]:
            left_index += 1
          while left_index < right_index and nums[right_index] == nums[right_index - 1]:
            right_index -= 1

          left_index += 1
          right_index -= 1
        elif current_sum < 0:
          left_index += 1
        else:
          right_index -= 1
    return answer
  
nums = [-1,0,1,2,-1,-4]
solution = Solution()
print(solution.threeSum(nums))

## Run Time: 683ms (Beats 65.53%) 
## Memory: 20.81mb (Beats 18.87%)
## Time Complexity: O(n^2)