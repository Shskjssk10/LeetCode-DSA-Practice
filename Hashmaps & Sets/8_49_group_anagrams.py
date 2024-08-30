class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    grouped_anagrams = []
    grouped_anagrams.append([strs[0]])
    if len(strs) == 1:  
      return grouped_anagrams 
    
    stored_dict = {}
    stored_dict[tuple(sorted(list(strs[0])))] = 0

    for word in strs[1:]:
      current_word_dict = tuple(sorted(list(word)))
      if current_word_dict in stored_dict:
        grouped_anagrams[stored_dict[current_word_dict]].append(word)
      else: 
        grouped_anagrams.append([word])
        stored_dict[current_word_dict] = len(stored_dict)
    return grouped_anagrams

    # stored_dict = {}
    # current_word_dict = {}
    # for letter in strs[0]:
    #   if letter not in current_word_dict:
    #     current_word_dict[letter] = 1 
    #   else:
    #     current_word_dict[letter] += 1
    # stored_dict[0] = current_word_dict

    # # Loops through strs
    # for word in strs[1:]:
    #   current_word_dict = {}
    #   # Makes a dict for each word
    #   for letter in word:
    #     if letter not in current_word_dict:
    #       current_word_dict[letter] = 1 
    #     else:
    #       current_word_dict[letter] += 1
    #   found_anagram = False

    #   # Compares to find for anagram 
    #   for index in stored_dict:
    #     if current_word_dict == stored_dict[index]:
    #       grouped_anagrams[index].append(word)
    #       found_anagram = True
    #       break
      
    #   # Appended to grouped_anagrams if no anagram is found
    #   if found_anagram is False:
    #     grouped_anagrams.append([word])
    #     stored_dict[len(stored_dict)] = current_word_dict
    # return grouped_anagrams

solution = Solution()
strs = ["stop","pots","reed","","tops","deer","opts",""]
print(solution.groupAnagrams(strs))

# Final Draft
## Run Time: 80ms (Beats 92.54%) 
## Memory: 20.55mb (Beats 43.383%)

# First Draft
## Run Time: 1849ms (Beats 5.03%) 
## Memory: 21.54mb (Beats 27.93%)