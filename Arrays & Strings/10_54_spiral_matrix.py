class Solution:
  def spiralOrder(matrix):
    length_of_matrix = sum(len(element) for element in matrix)
    bottom_wall = len(matrix)
    if bottom_wall == 0:
      return matrix[0]
    
    spiral_order = []
    start = 0
    right_wall = len(matrix[0])
    if right_wall == 1:
      for row in matrix:
        spiral_order.append(row[0])
      return spiral_order
    left_wall = 0
    top_wall = 0
    reversed_matrix = matrix[::-1]

    while True:
      # print(spiral_order)
      if len(spiral_order) == length_of_matrix:
        break
      
      # Appending numbers on the top
      spiral_order += matrix[top_wall][left_wall:right_wall]
      top_wall += 1
      if len(spiral_order) == length_of_matrix:
        break      

      # Appending numbers on the right
      for i in range(top_wall, bottom_wall):
        spiral_order.append(matrix[i][right_wall-1])
      if len(spiral_order) == length_of_matrix:
        break    

      # Appending numbers on the bottom
      spiral_order += matrix[bottom_wall-1][left_wall:right_wall-1][::-1]

      # Appending numbers on the left
      for i in range(top_wall, bottom_wall-1):
        spiral_order.append(reversed_matrix[i][left_wall])
      right_wall -= 1
      left_wall += 1
      bottom_wall -= 1

    return spiral_order


  matrix = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
  print(spiralOrder(matrix))

  ## Run Time: 33ms (Beats 73.42%) 
  ## Memory: 16.49mb (Beats 77.30%)