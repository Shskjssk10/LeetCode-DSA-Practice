class Solution:
  def isSubsequence(s, t) -> bool:
    s_length, t_length = len(s), len(t)
    if s == "": 
      return True
    if s_length > t_length:
      return False
    index = 0
    for letter in t: 
      if letter == s[index]:
        if index == s_length - 1:
          return True
        index += 1
    return False

  s, t = "abc", "ahbgdc"
  print(isSubsequence(s, t))  

  ## Run Time: 29ms (Beats 91.54%) 
  ## Memory: 16.38mb (Beats 99.52%)
  ## (I referred to someone's explanation)