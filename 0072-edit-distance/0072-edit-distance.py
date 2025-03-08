class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # going right is an insertion
        # going down is a deletion
        # going diagonal down-right is a replacement
        # each costs 1 operation

        # create a cache where word1 is the rows and word2 is
        # the columns 
        # initialize all costs as infinite to help w debugging
        cache = [[float('inf') for _ in range(len(word2) + 1)] \
            for _ in range(len(word1) + 1)]
        
        # fill out the bottom row
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        
        # fill out the last column
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        # fill out the cells, starting from the bottom right 
        # (almost; the bottom right "before" the true corner)
        # and then doing lines from right to left, 
        # working our way to the top
        for i in reversed(range(len(word1))):
            for j in reversed(range(len(word2))):
                # equal items are free
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j], \
                        cache[i][j+1], cache[i+1][j+1])

        return cache[0][0]