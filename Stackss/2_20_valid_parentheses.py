class Solution:
  def isValid(self, s: str) -> bool:
    if len(s) % 2 != 0:
      return False
    s = list(s)
    dictionary = { "(" : ")", "[": "]", "{": "}"}
    for i in range(int(len(s) / 2)):
      if len(s) == 0: 
        break
      character = s[0]
      if character not in dictionary: 
        return False
      elif dictionary[character] == s[-1]:
        s.pop()
        s.pop(0)
      elif dictionary[character] == s[1]:
        s.pop(0)
        s.pop(0)
      elif s[-2] in dictionary and dictionary[s[-2]] == s[-1]:
        s.pop()
        s.pop()
      else:
        return False
    return True
  
s = "[({(())}[()])]"
solution = Solution()
print(solution.isValid(s))