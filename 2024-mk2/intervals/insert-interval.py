class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # length 0 edge case
        if len(intervals) == 0:
            return [newInterval]
            
        # if newInterval needs to go at the beginning of intervals
        if intervals[0][0] > newInterval[0]:
            intervals.insert(0, newInterval)
        else:
            insertIdx = -1
            for i in range(len(intervals)-1):
                # put it before the interval it is <= to
                if intervals[i][0] <= newInterval[0] <= intervals[i+1][0]:
                    intervals = intervals[:i+1] + [newInterval] + intervals[i+1:]
                    break
    
            # Nowhere to go "between" elements
            # if first interval[0] is less than newInterval[0]
            if insertIdx == -1 and intervals[0][0] <= newInterval[0]:
                intervals.append(newInterval)
        
        # find overlaps
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                if intervals[i][1] <= intervals[i+1][1]:
                    intervals[i][1] = intervals[i+1][1]
                    intervals.pop(i+1)
                else:
                    intervals.pop(i+1)
            else:
                i+=1

        return intervals
        
