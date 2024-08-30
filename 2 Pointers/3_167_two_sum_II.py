class Solution:
  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    if len(numbers) == 2:
      return [1,2]
    for first_num in numbers[1:]: 
      diff = target - first_num
      if diff in numbers: 
        return [numbers.index(first_num) + 1, numbers.index(diff) + 1]

solution = Solution()
numbers = [2,3,4]
target = 6
print(solution.twoSum(numbers, target))