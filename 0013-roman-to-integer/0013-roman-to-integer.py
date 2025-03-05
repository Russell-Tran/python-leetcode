class Solution:
    def romanToInt(self, s: str) -> int:
        value = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        total = 0
        if not s:
            return 0
        offset = 0
        for i in reversed(range(len(s))):
            i = i + offset
            if i < 0:
                break

            char = s[i]
            if i == 0:
                total += value[char]
                continue
            
            char_next = s[i-1]
            if (
                (char == "V" or char == "X") and char_next == "I"  
                or (char == "L" or char == "C") and char_next == "X" 
                or (char == "D" or char == "M") and char_next == "C"
            ):
                total += value[char] - value[char_next]
                offset -= 1
            else:
                total += value[char]
        return total
            
