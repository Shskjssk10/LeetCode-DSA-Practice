class Solution:
  def summaryRanges(nums):
    sum_range = []
    if len(nums) == 0: return []
    if len(nums) == 1: return [f"{str(nums[0])}"]
    min = nums[0]
    flag = False ## True if it is consec with prev number
    sub_check = 1
    for i in range(1, len(nums[1:])+1):
      # print(min+sub_check != nums[i])
      if min+sub_check != nums[i]:
        if flag == False: sum_range.append(str(min)) ## Append single num
        else: sum_range.append(f"{min}->{nums[i-1]}") ## Append range
        if (nums[i] == nums[-1]): sum_range.append(str(nums[i])) ## Append single num when last number is reached
        sub_check = 1
        min = nums[i]
        flag = False
      else:
        if (nums[i] == nums[-1]): sum_range.append(f"{min}->{nums[i]}") # Append range when last number is reached
        sub_check += 1
        flag = True

    return sum_range
  sorted_list =[1,3]
  print(summaryRanges(sorted_list))

  ## Run Time: 34ms (Beats 61.39%) 
  ## Memory: 26.11mb (Beats 16.50%)