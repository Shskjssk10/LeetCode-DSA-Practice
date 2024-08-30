class Solution:
  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    if len(numbers) == 2:
      return [1,2]
    left_index = 0 
    right_index = len(numbers) - 1
    while True: 
      if numbers[left_index] + numbers[right_index] == target:
        return [left_index+1, right_index+1]
      if numbers[left_index] + numbers[right_index] < target:
        left_index += 1
      else: 
        right_index -= 1

    # for first_num in numbers: 
    #   diff = target - first_num
    #   if diff in numbers: 
    #     first_index = numbers.index(first_num) + 1
    #     return [first_index, numbers[first_index:].index(diff) + first_index + 1]

solution = Solution()
numbers = [5,25,75]
target = 100
print(solution.twoSum(numbers, target))

## Final Draft
## Run Time: 100ms (Beats 82.02%) 
## Memory: 17.73mb (Beats 39.71%)
## Time Complexity: O(n)

## First Draft
## Run Time: 5245ms (Beats 5.03%) 
## Memory: 17.70mb (Beats 83.57%)
## Time Complexity: O(n^2)