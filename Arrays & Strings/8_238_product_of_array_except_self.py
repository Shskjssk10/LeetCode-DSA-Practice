class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    product = 1
    no_of_zero = 0 
    for number in nums:
      if number == 0:
        no_of_zero += 1
      else:
        product *= number
    for i in range(len(nums)):
      if no_of_zero > 1: 
        nums[i] = 0
        continue
      if nums[i] == 0:
        nums[i] = int(product / 1)
      else: 
        if no_of_zero == 1: 
          nums[i] = 0 
        else: 
          nums[i] = int(product / nums[i])        
    return nums

solution = Solution() 
nums = [0,2,3,4]
print(solution.productExceptSelf(nums))

## Run Time: 258ms (Beats 86.93%) 
## Memory: 25.21mb (Beats 96.87%)
## Time Complexity: O(n)
## Space Complexity: O(1)