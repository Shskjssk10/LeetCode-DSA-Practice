class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    grouped_anagrams = []
    if len(strs) == 1:  
      grouped_anagrams.append(strs)
      return grouped_anagrams   
    
    return grouped_anagrams

solution = Solution()
strs = ["eat", 'something']
print(solution.groupAnagrams(strs))
