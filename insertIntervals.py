class Solution(object):
    def insert(self, intervals, newInterval):
        """
        57. Insert Interval
        You are given an array of non-overlapping intervals intervals where
        intervals[i] = [starti, endi] represent the start and the end of the
        ith interval and intervals is sorted in ascending order by starti. 
        You are also given an interval newInterval = [start, end] that represents
        the start and end of another interval.

        Insert newInterval into intervals such that intervals is still sorted in
        ascending order by starti and intervals still does not have any overlapping
        intervals (merge overlapping intervals if necessary).

        Return intervals after the insertion.

        Note that you don't need to modify intervals in-place. You can make a new array and return it.
        Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
        Output: [[1,5],[6,9]]

        Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
        Output: [[1,2],[3,10],[12,16]]
        Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]

        """
        # O(n)
        resultArray = []

        for current in range(len(intervals)):
            # Check if end of new interval is smaller than start of current interval
            if newInterval[1] < intervals[current][0]:
                resultArray.append(newInterval)
                return resultArray + intervals[current:]
            # Check if start of new interval is greater than start of current interval
            elif newInterval[0] > intervals[current][1]:
                resultArray.append(intervals[current])
            else:
                newInterval = [min(newInterval[0], intervals[current][0]), max(newInterval[1], intervals[current][1])]
        # Add the new inverval in case the new interval doesnt fall in any of the above scenarios
        # e.g. new interval = [] and to be inserted in any intervals
        resultArray.append(newInterval)

        return resultArray
