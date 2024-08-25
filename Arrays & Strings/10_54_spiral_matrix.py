class Solution:
  def spiralOrder(matrix):
    height = len(matrix)
    width = len(matrix[0])
    if height == 1:
      return matrix[0]
  matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
  print(spiralOrder(matrix))