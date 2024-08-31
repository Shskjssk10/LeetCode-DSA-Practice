class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    product = 1
    got_zero = False
    multiple_zero = False
    count = 0 
    for number in nums:
      if number == 0:
        got_zero = True
        count += 1
        if count == 2:
          multiple_zero = True
      else:
        product *= number
    for i in range(len(nums)):
      if multiple_zero: 
        nums[i] = 0
        continue
      if nums[i] == 0:
        nums[i] = int(product / 1)
      else: 
        if got_zero: 
          nums[i] = 0 
        else: 
          nums[i] = int(product / nums[i])        
    return nums

solution = Solution() 
nums = [0,2,3,4]
print(solution.productExceptSelf(nums))

## Run Time: 267ms (Beats 61.33%) 
## Memory: 25.04mb (Beats 98.39%)