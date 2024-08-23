class Solution:
  def twoSum(nums, target: int):
    dictionary = {}
    for i in range(len(nums)):
      dictionary[nums[i]] = i
    for i in range(len(nums)):
      second_num = target - nums[i]
      if second_num in dictionary and dictionary[second_num] != i:
        return [i, dictionary[second_num]]

    # index = 0
    # for first_num in nums[:len(nums)-1]: 
    #   index += 1
    #   for second_num in nums[nums.index(first_num)+1:]:
    #     print(nums[nums.index(first_num)+1:])
    #     if first_num+second_num == target:
    #       return [nums.index(first_num), nums[nums.index(first_num)+1:].index(second_num)+index]

  nums = [2,7,11,15]
  target = 9
  print(twoSum(nums, target))

  # FYI: I Cheated, I had no idea how to make the time complexity anywhere better than O(n^2)

  ## Run Time: 57ms (Beats 73.04%) 
  ## Memory: 17.65mb (Beats 54.77%)
