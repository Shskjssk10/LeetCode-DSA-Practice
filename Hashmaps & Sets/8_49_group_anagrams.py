class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    grouped_anagrams = []
    index = 1
    for word in strs:
      word_dictionary = {}
      for letter in word: 
        if letter not in word_dictionary:
          word_dictionary[letter] = 1
        else: 
          word_dictionary[letter] += 1
      print(word_dictionary)
      strs.remove(word)
      got_anagram = False
      # Checking for anagrams in list 
      for check_word in strs[index:]:
        # Checking for anagrams
        for letter in check_word:
          # If word is anagram
          if len(word_dictionary) == 0:
            grouped_anagrams.append([word, check_word])
            strs.remove(check_word)
            got_anagram = True
            break
          if letter not in word_dictionary:
            break
          elif word_dictionary[letter] == 1:
            del word_dictionary[letter]
          else:
            word_dictionary[letter] -= 1
        index += 1
      if got_anagram is False:
        grouped_anagrams.append([word])

      
    return grouped_anagrams

solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(strs))
