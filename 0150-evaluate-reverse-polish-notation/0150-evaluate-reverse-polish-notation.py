class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set("+-*/")

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                right, left = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    stack.append(int(left / right))
                else:
                    raise ValueError(token)

        return stack[0]

"""
so looks like, like normal when dealing with expressions or grammars,
you need recursive behavior or stack-simulated recursion

use left hand and right hand and then operation together, then store in left hand

of course, if the expression gets too long, then store half-completed left hands on the stack or something

looks like, with an operator, you look at the last 2 integers than came right before it, then that's how you order your operations

so the stack should be made of numbers, then pop the last 2 to do the operation it seems

["2","1","+","3","*"]
push 2 push 1
pop 1 (right) pop 2 (left) add
push result down

push 3
pop 3 pop (2 + 1)

["4","13","5","/","+"]
push 4
push 13
push 5
pop 5 (right)
pop 13 (left)
divide
push result 
pop that (right)
pop 4 (left)
add
push result

stream is done so return the one and only integer in the stack


python is int??? or just do in sets for both the ints and the operators
"""