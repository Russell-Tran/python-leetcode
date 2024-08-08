class Solution:
    
    def grow(self, s, start_index):
        output = s[start_index]
        left_idx = start_index - 1
        right_idx = start_index + 1
        while left_idx >= 0 and right_idx < len(s) and s[left_idx] == s[right_idx]:
            output = s[left_idx] + output + s[right_idx]
            left_idx -= 1
            right_idx += 1
        return output
    
    def grow_even(self, s, start_index):
        output = ''
        left_idx = start_index - 1
        right_idx = start_index
        while left_idx >= 0 and right_idx < len(s) and s[left_idx] == s[right_idx]:
            output = s[left_idx] + output + s[right_idx]
            left_idx -= 1
            right_idx += 1
        return output
    
    def longestPalindrome(self, s: str) -> str:
        batch = []
        
        # From each character, grow outwards
        for index in range(len(s)):
            batch.append(self.grow(s, index))
            if index > 0:
                batch.append(self.grow_even(s, index))
        
        # Pick the longest in the batch
        length = max([len(x) for x in batch])
        for x in batch:
            if len(x) == length:
                return x