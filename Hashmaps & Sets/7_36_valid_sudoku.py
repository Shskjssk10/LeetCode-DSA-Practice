class Solution:
  def isValidSudoku(self, board: list[list[str]]) -> bool:
    #Checking rows
    for i in range(9):
      check_set = set()
      for element in board[i]:
        if element != '.' and element in check_set:
          print("row check fail")
          return False
        elif element != '.':
          check_set.add(element)
    
    #Checking columns
    for i in range(9):
      check_set = set()
      for row in board:
        if row[i] != '.' and row[i] in check_set:
          print("column check fail")
          return False
        elif row[i] != '.':
          check_set.add(row[i])

    #Checking Boxes
    box_check_coords = [[0,3],[3,6],[6,9]]
    for i in range(3):
      rows = board[box_check_coords[i][0]: box_check_coords[i][1]]
      for coords in box_check_coords:
        check_set = set()
        for row in rows:
          for element in row[coords[0]:coords[1]]:
            # print(row[coords[0]:coords[1]])
            if element != '.' and element in check_set:
              # print(f"loop: {i} box: {coords} box check fail")
              return False
            elif element != '.':
              check_set.add(element)
    

    return True
  
board = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
solution = Solution()
print(solution.isValidSudoku(board))

  ## Run Time: 89ms (Beats 74.81%) 
  ## Memory: 16.52mb (Beats 50.10%)