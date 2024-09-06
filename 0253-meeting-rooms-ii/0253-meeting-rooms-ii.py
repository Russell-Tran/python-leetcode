class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1
        
        intervals = sorted(intervals)
        trains = [[]]
        trains[0].append(intervals.pop(0))
        
        def find_minimum_gap_idx(trains, candidate):
            gaps = [candidate - train[-1][-1] for train in trains]
            failed_trains = 0
            for i in range(len(gaps)):
                if gaps[i] < 0:
                    gaps[i] = float('inf')
                    failed_trains += 1
            if failed_trains == len(trains):
                return -1
            return gaps.index(min(gaps))
            
        for interval in intervals:
            min_gap_idx = find_minimum_gap_idx(trains, interval[0])
            if min_gap_idx == -1:
                trains.append([interval])
            else:
                trains[min_gap_idx].append(interval)
        
        
        return len(trains)