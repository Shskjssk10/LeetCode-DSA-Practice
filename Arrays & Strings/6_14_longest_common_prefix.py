class Solution:
  def longestCommonPrefix(strs) -> str:
    if len(strs) == 1: return strs[0]
    prefix = strs[0]
    for word in strs[1:]:
      index = 0
      if len(prefix) == 0: return ""
      for letter in prefix:
        if index == len(word): break
        if letter != word[index]: break
        index += 1
      prefix = prefix[:index]
    return prefix

    # First Draft
    # if len(strs) == 1: return strs[0]
    # prefix = strs[0]
    # for word in strs[1:]:
    #   index = 0
    #   if len(prefix) == 0:
    #     return ""
    #   for letter in word: 
    #     if index == len(prefix): break
    #     if letter != prefix[index]: break
    #     index += 1
    #   prefix = prefix[:index]
    # return prefix
  
  strs = ["flower","flow","flight"]
  print(longestCommonPrefix(strs))

  ## First Draft
  ## Run Time: 42ms (Beats 26.96%) 
  ## Memory: 29.37mb (Beats 29.37%)

  ## Final Draft
  ## Run Time: 30ms (Beats 93.59%) 
  ## Memory: 16.56mb (Beats 68.74%)