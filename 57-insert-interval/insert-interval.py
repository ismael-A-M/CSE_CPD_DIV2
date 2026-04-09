from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        b = [intervals[0]]

        for h, v in intervals[1:]:
            last = b[-1][1]
            if h <= last:
                b[-1][1] = max(last, v)
            else:
                b.append([h, v])
        
        return b