class Solution:
    def _recurse(self, result, n, num_open, num_close, constr):
        if n == num_open == num_close:
            result.append(constr)
            return

        if num_open < n:
            self._recurse(result, n, num_open+1, num_close, constr + '(')

        if num_close < num_open:
            self._recurse(result, n, num_open, num_close+1, constr + ')')

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self._recurse(result, n, 0, 0, "")
        return result

