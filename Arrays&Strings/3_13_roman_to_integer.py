class Solution:
  def romanToInt(s) -> int:
    total = 0
    roman_keys = {
      "I":1,
      "IV":4,
      "V":5,
      "IX":9,
      "X":10,
      "XL":40,
      "L":50,
      "XC":90,
      "C":100,
      "CD":400,
      "D":500,
      "CM":900,
      "M":1000
    }
    iterations = len(s)
    for i in range(iterations):
      if len(s) == 0:
        break
      if len(s) > 1 and (roman_keys.get(s[0]) < roman_keys.get(s[1])):
        total += roman_keys.get(s[0] + s[1])
        s = s.replace(s[0] + s[1],"",1)
      else: 
        total += roman_keys.get(s[0])
        s = s.replace(s[0],"",1)
    return total
  
  s="III"
  print(romanToInt(s))

  ## Run Time: 41ms (Beats 83.39%) 
  ## Memory: 16.56mb (Beats 43.99%)

