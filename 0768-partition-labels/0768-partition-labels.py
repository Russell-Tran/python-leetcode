class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []

        # Phase 1: prospecting phase
        intervals = {} # char -> [start, stop)
        for i, char in enumerate(s):
            if char not in intervals:
                intervals[char] = [i, i + 1]
            else:
                intervals[char][1] = i + 1

        # Phase 2: meeting needs phase
        needs = list(sorted(intervals.values()))
        start, stop = 0, 1
        for need_start, need_stop in needs:
            if need_start >= stop:
                result.append(stop - start)
                start, stop = need_start, need_stop
            else:
                stop = max(stop, need_stop)
        result.append(stop - start)

        return result





"""JUNK
        result = []
        seen = set()
        count = 0
        for char in s:
            if char not in seen:
                seen.add(char)
                count += 1
            else:
                result.append(count)
                seen = set()
                seen.add(char)
                count = 1
        if count > 0:
            result.append(count)
        return result
"""
        
        