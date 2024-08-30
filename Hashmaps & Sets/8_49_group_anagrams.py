class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    grouped_anagrams = []
    grouped_anagrams.append([strs[0]])
    if len(strs) == 1:  
      return grouped_anagrams 
    for word in strs[1:]:
      anagram_found = False
      for group in grouped_anagrams:
        potential_anagram = {}
        # Dictionary for potential anagram  
        if len(group[0]) == 0 and len(word) == len(group[0]):
          anagram_found = True 
          group.append(word)
          break
        for letter in group[0]:
          if letter not in potential_anagram:
            potential_anagram[letter] = 1 
          else:
            potential_anagram[letter] += 1
        # Checking if word is anagram
        for letter in word: 
          if letter not in potential_anagram:
            break
          elif potential_anagram[letter] == 1 and len(potential_anagram) == 1:
            group.append(word)
            anagram_found = True
            break
          elif potential_anagram[letter] == 1:
            del potential_anagram[letter]
          else:
            potential_anagram[letter] -= 1
        if anagram_found:
          break
      if anagram_found is False:
        grouped_anagrams.append([word]) 
    return grouped_anagrams

solution = Solution()
strs = ["",""]
print(solution.groupAnagrams(strs))
