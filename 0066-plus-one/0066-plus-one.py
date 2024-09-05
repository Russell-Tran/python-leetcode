class Solution:
    
    def carry_over(self, digits, i):
        if digits[i] < 10:
            return
        else:
            digits[i] %= 10
            i -= 1
            if i < 0: # hits -1
                digits.insert(0, 0)
                i = 0
            digits[i] += 1
            self.carry_over(digits, i)
        
    
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        digits[i] += 1
        self.carry_over(digits, i)
        return digits