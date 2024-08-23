class Solution:
  ## Where word1 and word2 are str type
  def mergeAlternately(word1, word2) -> str:
    max_iteration = max(len(word1), len(word2))
    # print(type(max_iteration))
    merged_string = ""
    for i in range(max_iteration):
      if i < len(word1):
        merged_string += f"{word1[i]}"
      if i < len(word2):
        merged_string += f"{word2[i]}"
    return merged_string

  word1, word2 = "abc", "pqr"
  merged_string = mergeAlternately(word1, word2)
  print(merged_string)

  ## Run Time: 34ms (Beats 66.69%) 
  ## Memory: 16.40mb (Beats 95.78%)