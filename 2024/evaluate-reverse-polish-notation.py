class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def add(x, y):
            return x + y
        def sub(x, y):
            return x - y
        def mult(x, y):
            return x*y
        def div(x, y):
            return int(x/y)
        ops = ['+', '-', '*', '/']
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                if token == '+':
                    y = stack.pop()
                    x = stack.pop()
                    stack.append(add(x, y))
                elif token == '-':
                    y = stack.pop()
                    x = stack.pop()
                    stack.append(sub(x, y))
                elif token == '*':
                    y = stack.pop()
                    x = stack.pop()
                    stack.append(mult(x, y))
                elif token == '/':
                    y = stack.pop()
                    x = stack.pop()
                    stack.append(div(x, y))

        return stack.pop()