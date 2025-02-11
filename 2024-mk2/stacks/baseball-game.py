class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            print(stack)
            if op == '+':
                one = stack.pop()
                two = stack.pop()
                stack.append(two)
                stack.append(one)
                stack.append(one+two)
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                num = stack.pop()
                stack.append(num)
                stack.append(num*2)
            else:
                stack.append(int(op))

        return sum(stack)
        
