class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        snake_collection = set()
        tail_idx, head_idx = 0, 1
        snake_collection.add(s[tail_idx])

        longest = len(snake_collection)

        while head_idx < len(s):
            char = s[head_idx]
            while char in snake_collection:
                snake_collection.remove(s[tail_idx])
                tail_idx += 1  
            snake_collection.add(char)
            longest = max(longest, len(snake_collection))
            head_idx += 1

        return longest

        
"""
wait isnt this just a running set or , oh i see, mayb ea two pointers solution
because , it's yeah it's the snake game one right, in which case i've seen this
in an interview before
"""