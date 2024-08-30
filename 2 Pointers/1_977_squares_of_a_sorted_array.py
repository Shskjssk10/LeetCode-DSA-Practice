class Solution:
  def sortedSquares(self, nums: list[int]) -> list[int]:
    result = []
    for number in nums: 
      result.append(number**2)
    result.sort()  
    return result

solution = Solution()
nums = [-4,-1,0,3,10]
print(solution.sortedSquares(nums))

## Run Time: 149ms (Beats 80.65%) 
## Memory: 18.71mb (Beats 59.10%)