class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # algorithm:
        # expandable list of vertical vectors
        matrix = []

        # if numRows == 1
        if numRows == 1:
            return s

        # if the numRows is == 2 then can handle specially:
        elif numRows == 2:
            i = 0
            while i < len(s):
                vector = [s[i], s[i+1] if i + 1 < len(s) else ""]
                matrix.append(vector)
                i += 2
            
        # normal behavior
        else:
            # until all characters consumed:
            fillOutMode = True
            stairIndex = numRows - 2
            i = 0
            while i < len(s):
                curr_vector = ["" for _ in range(numRows)]
                if fillOutMode:
                    # fill out the row length as a vector
                    for q in range(numRows):
                        if i < len(s):
                            curr_vector[q] = s[i]
                            i += 1
                    fillOutMode = False
                else:
                    # starting from i = len() - 2, create 1-char vectors
                    # while we are not i = 0
                    curr_vector[stairIndex] = s[i]
                    stairIndex -= 1
                    i += 1

                    if stairIndex == 0:
                        fillOutMode = True
                        stairIndex = numRows - 2

                matrix.append(curr_vector)
            
        # reconstitute string linearly
        result = ""
        for w in range(numRows):
            for vector in matrix:
                result += vector[w]

        return result
