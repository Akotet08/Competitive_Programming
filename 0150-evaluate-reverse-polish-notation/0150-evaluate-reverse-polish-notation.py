class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '/', '*'])

        for i in tokens:
            if i in operators:
                op1 = stack.pop()
                op2 = stack.pop()

                result = self.compute(op2, op1, i)
                stack.append(result)
            else:
                stack.append(int(i))

        return stack[0]
    
    def compute(self, op1, op2, operator):
        if operator == '+':
            return op1 + op2
        if operator == '*':
            return op1 * op2
        if operator == '/':
            return int(op1 / op2)
        if operator == '-':
            return op1 - op2