class Solution:
  def canConstruct(ransomNote, magazine) -> bool:
    ransom_dict = {}
    for letter in ransomNote:
      if letter not in ransom_dict:
        ransom_dict[letter] = 1
      else: 
        ransom_dict[letter] += 1

    magazine_dict = {}
    for letter in magazine:
      if magazine_dict == ransom_dict:
        return True
      if (letter not in magazine_dict and 
          letter in ransomNote):
        magazine_dict[letter] = 1
      elif letter in magazine_dict: 
        magazine_dict[letter] += 1

    # print(ransom_dict)
    # print(magazine_dict)
    #Check if True
    if len(magazine_dict) != len(ransom_dict):
      return False 
    # print(magazine_dict)
    for magazine_key in magazine_dict.keys():
      if magazine_dict[magazine_key] < ransom_dict[magazine_key]:
        return False
    return True

  
  ransomNote = "bg"
  magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"

  print(canConstruct(ransomNote, magazine))

  ## Run Time: 80ms (Beats 7.55%) 
  ## Memory: 16.67mb (Beats 63.09%)