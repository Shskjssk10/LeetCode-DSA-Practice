class Solution:
  def summaryRanges(nums):
    sum_range = []
    if len(nums) == 0: return []
    if len(nums) == 1: return [f"{str(nums[0])}"]
    min = nums[0]
    flag = False
    sub_check = 1
    for i in range(1, len(nums[1:])+1):
      # print(min+sub_check != nums[i])
      if min+sub_check != nums[i]:
        if flag == False: sum_range.append(str(min))
        else: sum_range.append(f"{min}->{nums[i-1]}")
        if (nums[i] == nums[-1]): sum_range.append(str(nums[i]))
        sub_check = 1
        min = nums[i]
        flag = False
      else:
        if (nums[i] == nums[-1]): sum_range.append(f"{min}->{nums[i]}")
        sub_check += 1
        flag = True

    return sum_range
  sorted_list =[1,3]
  print(summaryRanges(sorted_list))

  ## Run Time: 38ms (Beats 31.63%) 
  ## Memory: 16.49mb (Beats 67.16%)