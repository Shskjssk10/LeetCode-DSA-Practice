class Solution:
  def maxNumberOfBalloons(text) -> int:
    if len(text) < 7:
      return 0
    balloon_set = set("balloon")
    dictionary = {}
    for letter in text:
      if (letter not in dictionary 
          and letter in balloon_set):
        dictionary[letter] = 1
      elif letter in balloon_set:
        dictionary[letter] += 1

    for letter in "lo":
      if letter not in dictionary: 
        return 0
      else: 
        dictionary[letter] //= 2
      
    # print(dictionary)
    return min(dictionary.values())
  text = "loonbalxballpoon"
  print(maxNumberOfBalloons(text))

  ## Run Time: 33ms (Beats 82.91%) 
  ## Memory: 16.94mb (Beats 94.79%)