class Solution:
  def findClosestNumber(nums) -> int:
    if len(nums) == 1: 
      return nums[0]
    closest_number = nums[0]
    for number in nums[1:]:
      if abs(number) < abs(closest_number): 
        closest_number = number
      if (abs(number) == abs(closest_number)) and (closest_number < number): 
        closest_number = number
    return closest_number
  
    # The difference between the final and second draft is the fact that the if else statements 
    # are not compressed into a single line.

    # Second Draft
    # if len(nums) == 1: return nums[0]
    # closest_number = nums[0]
    # for number in nums[1:]:
    #   if abs(number) < abs(closest_number): closest_number = number
    #   if (abs(number) == abs(closest_number)) and (closest_number < number): closest_number = number
    # return closest_number

    # First Draft
    # closest_number, closest_distance = nums[0],abs(nums[0])
    # for number in nums[1:]: 
    #   absolute_number = abs(number)
    #   if absolute_number < closest_distance: 
    #     closest_number, closest_distance = number, absolute_number
    #   if absolute_number == closest_distance and number > closest_number:
    #     closest_number = number
    # return closest_number

  nums = [2,1,1,-1,100000]
  output = findClosestNumber(nums)
  print(output)

## First Draft
## Run Time: 122ms (Beats 49.83%) 
## Memory: 16.59mb (Beats 99.26%)

## Second Draft
## Run Time: 121ms (Beats 55.83%) 
## Memory: 16.76mb (Beats 60.47%)

## Final Draft
## Run Time: 121ms (Beats 99.95%) 
## Memory: 16.76mb (Beats 60.47%)

## FYI: I did this without ANY DSA knowledge whatsoever, just plain Python knowledge.