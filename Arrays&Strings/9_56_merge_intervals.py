class Solution:
  def merge(intervals):
    intervals = sorted(intervals)
    merged_intervals = [intervals[0]]
    if len(intervals) == 1:
      return merged_intervals
    for i in range(1,len(intervals)):
      # Checks if last appended second num is bigger than current list first num
      if merged_intervals[-1][1] >= intervals[i][0]:
        # Takes the bigger number of the two respective positions
        merged_intervals.append([merged_intervals[-1][0], 
                                max(intervals[i][1], merged_intervals[-1][1])])
        merged_intervals.pop(-2)
      else: 
        merged_intervals.append(intervals[i])
    return merged_intervals
  
  intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
  print(f"Merged Intervals: {merge(intervals)}")

  ## Run Time: 122ms (Beats 63.99%) 
  ## Memory: 20.62mb (Beats 50.33%)

  # Model Solution (By Greg Hogg YT Channel)
  # class Solution:
  #   def merge(self, intervals: List[List[int]]) -> List[List[int]]:
  #       intervals = sorted(intervals)
  #       merged_intervals = []
  #       for interval in intervals:
  #           if not merged_intervals or merged_intervals[-1][1] < interval[0]:
  #               merged_intervals.append(interval)
  #           else: 
  #               merged_intervals[-1] = [merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1])]
  #       return merged_intervals

## Greg Hogg's Solution
## Run Time: 119ms (Beats 78.02%) 
## Memory: 20.60mb (Beats 69.43%)

