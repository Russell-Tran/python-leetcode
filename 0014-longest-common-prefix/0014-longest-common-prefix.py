class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        O(k * n), where k is the length of the shortest string and n is the length of the array of strings
        """

        j = 0
        if not strs or not strs[0]:
            return ""

        if len(strs) == 1:
            return strs[0]
        
        output = ""
        for j in range(min([len(string) for string in strs])):
            for i in range(1, len(strs)):
                if strs[i][j] != strs[i-1][j]:
                    return output
            output += strs[0][j]

        return output



    
    """
        lcp = ""
        grow_idx = 0
        minimum = min([len(string) for string in strs])

        if not strs or len(strs[0]) == 0:
            return ""
        lcp = strs[0][0]

        for i, string in enumerate(strs):
            char = string[grow_idx]
            if char != lcp[-1]:
                return lcp
            if i == len(strs) - 1:
                lcp += char
                if grow_idx < minimum:
                    grow_idx += 1
                else:
                    return lcp

        return lcp

    """