import math
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_side_len = len(board)
        subgrid_side_len = int(math.sqrt(board_side_len))
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(board_side_len):
            for j in range(board_side_len):
                val = board[i][j]
                if val == '.':
                    continue
                elif val in row_sets[i]:
                    return False
                elif val in col_sets[j]:
                    return False
                elif val in subgrid_sets[i // subgrid_side_len][j // subgrid_side_len]:
                    return False
                else:
                    row_sets[i].add(val)
                    col_sets[j].add(val)
                    subgrid_sets[i // subgrid_side_len][j // subgrid_side_len].add(val)
        return True


"""
ANKI
- COMMON SENSE YES: Hash sets for each row, column, and subgrid. Could talk about traversal vs storage tradeoffs. Btw the way to make the subgrid sets easy is to store those as its own grid of sets and // by the subgtide side len

- ALT1: Array of fixed length that stores "seen" booleans. can use the soduku vals as indices to jump around.
And basically do that for each row , col, subgrid like before , this is actually the same thing as hashing

- ALT2: Store these "seen" booleans as binaries in bits, and use bitmasking and bit logic to compress all
of this into integers instead of arrays or sets.

NOTES
I've seen this as a company problem before, and choked, so it's a good one to cover 
(Actually I think the problem was a sudoku solver instead, or a minesweeper solver,
or to build minesweeper)

Seems like the approach would be to maintain sets while traversing the cells 

If you want to maximally conserve space, just have one set at a time and overwrite it as you
traverse rows, then re-traverse columns, then re-traverse subboxes. That's kind of overkill though

If you want to minimally use compute, I'd have 9 sets for the 9 rows, 9 sets for the 9 columns, 9 sets
for the 9 subboxes, simultaneously, and check each as you go. 

If you want a happy medium, then mix and match this. 

I think the easiest way to write this it to have all the sets ready.
"""