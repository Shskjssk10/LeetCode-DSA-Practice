class Solution:
  def spiralOrder(matrix):
    length_of_matrix = [len(element) for element in matrix]
    bottom_wall = len(matrix)
    if bottom_wall == 1:
      return matrix[0]
    
    spiral_order = []
    start = 0
    right_wall = len(matrix[0])
    left_wall = 0
    top_wall = 0
    reversed_matrix = matrix[::-1]
    while True:
      print(spiral_order)
      if len(spiral_order) == length_of_matrix:
        return spiral_order
      
      # Appending numbers on the top
      spiral_order += matrix[top_wall][left_wall:right_wall]
      print(spiral_order, "After top numbers added")
      top_wall += 1
      if len(spiral_order) == length_of_matrix:
        return spiral_order
      
      # Appending numbers on the right
      for i in range(top_wall, bottom_wall):
        spiral_order.append(matrix[i][right_wall-1])
      print(spiral_order, "After right numbers added")

      # Appending numbers on the bottom
      print(bottom_wall)
      print(reversed_matrix[bottom_wall])
      spiral_order += matrix[:bottom_wall:-1][right_wall:left_wall]
      print(spiral_order, "After bottom numbers added")

      # Appending numbers on the left
      for i in range(top_wall, bottom_wall):
        spiral_order.append(reversed_matrix[i][left_wall])
      left_wall += 1
      right_wall -= 1
      bottom_wall -= 1
      


    
  matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
  print(spiralOrder(matrix))