class Solution:
    def sum_of_squares_of_digits(self, n):
        summation = 0
        while n > 0:
            digit = n % 10 
            summation += digit * digit
            n //= 10
        return summation
    
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            if n == 1:
                return True
            n = self.sum_of_squares_of_digits(n)
        return False
        