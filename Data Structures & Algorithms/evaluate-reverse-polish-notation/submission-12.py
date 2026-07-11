class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "*": 
                op1, op2 = stack.pop(), stack.pop()
                stack.append( op1 * op2 )
            elif tokens[i] == "+":
                op1, op2 = stack.pop(), stack.pop()
                stack.append( op1 + op2 )
            elif tokens[i] == "-":
                op1, op2 = stack.pop(), stack.pop()
                stack.append( op2 - op1 )
            elif tokens[i] =="/":
                op1, op2 = stack.pop(), stack.pop()
                stack.append( int(op2 / op1))
            else:
                stack.append(int(tokens[i]))
    # resu = stack.pop()    
        return stack.pop()

