class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals or len(intervals) == 1:
            return True
        # sort by start times
        intervals = sorted(intervals)
        # assert whether it's ascending order
        curr = intervals[0][0]
        for interval in intervals:
            for timestamp in interval:
                if timestamp < curr:
                    return False
                curr = timestamp
        return True