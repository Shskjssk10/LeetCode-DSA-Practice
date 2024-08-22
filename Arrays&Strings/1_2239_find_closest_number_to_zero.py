class Solution:
  def findClosestNumber(nums) -> int:
    closest_number, closest_distance = nums[0],abs(nums[0])
    for number in nums[1:]: 
      absolute_number = abs(number)
      if absolute_number < closest_distance: 
        closest_number, closest_distance = number, absolute_number
      if absolute_number == closest_distance and number > closest_number:
        closest_number = number
    return closest_number

  nums = [2,-1,1]
  output = findClosestNumber(nums)
  print(output)

## Run Time: 122ms (Beats 49.83%) 
## Memory: 16.59mb (Beats 99.26%)

## FYI: I did this without ANY DSA knowledge whatsoever, just plain Python knowledge.