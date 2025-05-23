class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        opener = set(['(', '{', '['])
        opener_of = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for char in s:
            if char in opener:
                stack.append(char)
            else:
                if not stack or stack[-1] != opener_of[char]:
                    return False
                stack = stack[:-1]

        return not stack



"""
([)]


"""

"""
JUNK (BAD):

        if not s:
            return True

        open_counts = {
            '(' : 0,
            '{' : 0,
            '[' : 0
        }

        opener = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for char in s:
            if char in open_counts:
                open_counts[char] += 1
            else:
                opposite = opener[char]
                if open_counts[opposite] <= 0:
                    return False
                else:
                    open_counts[opposite] -= 1

        return all(count == 0 for count in open_counts.values())
"""