class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best_length = 0
        tail_idx = 0
        head_idx = 0
        letters = set()
        # probe forward
        for i in range(len(s)):
            letter = s[i]
            substring = s[tail_idx:head_idx]
            
            # candidate already exists
            if letter in letters:
                # shrink the tail
                for j in range(0, substring.find(letter)):
                    discard_letter = substring[j]
                    letters.remove(discard_letter)
                tail_idx += substring.find(letter)+1
            
            head_idx += 1
            letters.add(letter)
            best_length = max(best_length, head_idx - tail_idx)
               
        return best_length