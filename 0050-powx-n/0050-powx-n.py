class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            cache = {0:1, 1: x}
            power = 2
            curr = x
            while power <= n:
                curr = curr * curr
                cache[power] = curr
                power *= 2

            powers = reversed(sorted(cache.keys()))
            output = 1
            def biggest_acceptable(w):
                for power in powers:
                    if w >= power:
                        return power

            while n > 0:
                power = biggest_acceptable(n)
                output *= cache[power]
                n -= power

            return output
        else:
            cache = {0:1, -1: 1/x}
            power = -2
            curr = 1/x
            while power >= n:
                curr = curr * curr
                cache[power] = curr
                power *= 2

            powers = sorted(cache.keys())
            output = 1
            def smallest_acceptable(w):
                for power in powers:
                    if w <= power:
                        return power

            while n < 0:
                power = smallest_acceptable(n)
                output *= cache[power]
                n -= power

            return output