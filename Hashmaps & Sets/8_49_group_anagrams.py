class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    grouped_anagrams = []
    grouped_anagrams.append([strs[0]])
    if len(strs) == 1:  
      return grouped_anagrams 
    for word in strs[1:]:
      current_word = {}
      for letter in word:
          if letter not in current_word:
            current_word[letter] = 1 
          else:
            current_word[letter] += 1
      anagram_found = False
      for group in grouped_anagrams:
        potential_anagram = {}
        # Dictionary for potential anagram  
        if len(group[0]) == 0 and len(word) == len(group[0]):
          print("this got run")
          anagram_found = True 
          group.append(word)
          break
        for letter in group[0]:
          if letter not in potential_anagram:
            potential_anagram[letter] = 1 
          else:
            potential_anagram[letter] += 1
        # Checking if word is anagram
        if len(word) != len(group[0]):
          continue
        if current_word == potential_anagram:
          anagram_found = True
          group.append(word)
      if anagram_found is False:
        grouped_anagrams.append([word]) 
    return grouped_anagrams
solution = Solution()
strs = ["stop","pots","reed","","tops","deer","opts",""]
print(solution.groupAnagrams(strs))
# print(solution.make_dictionary("stop"))
# print(solution.make_dictionary("pots"))