import operator
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        dic = {
            '+':operator.add,
            '-':operator.sub,
            '*':operator.mul,
            '/':operator.truediv}
        
        for token in tokens:
            if token not in dic:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                result = int(dic[token](b,a))
                stack.append(result)

                    
        return stack[0]
        