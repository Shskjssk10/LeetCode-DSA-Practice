class Solution:
  def containsDuplicate(nums) -> bool:
    unique_keys = set(nums)
    nums_dict = {}
    for key in unique_keys: 
      nums_dict[key] = 0
    for num in nums: 
      if num in nums_dict:
        if nums_dict[num] == 1:
          return True
        nums_dict[num] += 1
    # print(nums_dict)
    return False
  
  nums = [1,2,3,1]
  print(containsDuplicate(nums))

  ## Run Time: 429ms (Beats 25.62%) 
  ## Memory: 28.79mb (Beats 15.57%)

  # Model Solution (By Greg Hogg YT Channel)
  # h = set()
  # for num in nums:
  #   if num in h:
  #     return True
  #   else:
  #     h.add(num)
  # return False

  ## Run Time: 413ms (Beats 73.35%) 
  ## Memory: 31.93mb (Beats 47.18%)