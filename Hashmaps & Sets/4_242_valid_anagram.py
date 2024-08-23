class Solution:
  def isAnagram(s, t) -> bool:
    if len(s) != len(t):
      return False
    dictionary = {}
    for letter in s: 
      if letter not in dictionary:
        dictionary[letter] = 1
      else: 
        dictionary[letter] += 1
    
    for letter in t:
      if letter not in dictionary:
        return False
      elif dictionary[letter] == 1:
        del dictionary[letter]
      else:
        dictionary[letter] -= 1

    return True
  
  s = "dell"
  t = "nagaram"

  print(isAnagram(s, t))

  ## Run Time: 42ms (Beats 86.58%) 
  ## Memory: 16.94mb (Beats 46.13%)