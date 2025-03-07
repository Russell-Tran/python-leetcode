from collections import defaultdict
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations = list(sorted(citations))

        # remove zeros since they are useless
        prefix_truncate = 0
        for i in range(len(citations)):
            if citations[i] != 0:
                prefix_truncate = i
                break

        citations = list(reversed(citations[prefix_truncate:]))

        for i, citation in enumerate(citations):
            # compare counts
            # ensures highest h returned
            if i + 1 >= citation:
                # return either this h score or the 
                # candidate h score of everything right before this
                return max(min(citation, i + 1), min(citations[i-1], i))
        # situations where the references are higher than the papers
        return min(citations[-1], len(citations))



"""
Junk
        tally = defaultdict(int)
        for citation in citations:
            tally[citation] += 1
        
        champion = 0
        for paper, count in tally.items():
            if count >= paper and paper > 
        return champion

"""