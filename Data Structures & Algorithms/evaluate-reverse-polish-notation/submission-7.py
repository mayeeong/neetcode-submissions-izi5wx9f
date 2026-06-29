import operator
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        dict_operands = {"*": operator.mul, "-": operator.sub, "+": operator.add, "/": operator.truediv}
        for x in tokens:
            if x.lstrip('-').isdigit():
                stack.append(int(x))
            else:
                x1 = stack.pop()
                x2 = stack.pop()
                operand = dict_operands[x](x2,x1)
                stack.append(int(operand))


        
        return stack[0]
        

        