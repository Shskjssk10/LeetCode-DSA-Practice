class Solution:
  def removeDuplicates(self, nums: list[int]) -> int:
    marker = 0

    for num in nums[1:]:
      if num > nums[marker]:
        nums[marker] = num
      else:
        marker += 1
    
    print(nums)
    return marker + 1
  
solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
k = solution.removeDuplicates(nums)

print(k)