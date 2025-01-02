class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        # Stacks are good for processing things related to time
        # This will keep (temp, index)
        stack = []

        for idx, temp in enumerate(temperatures):
            # While there is a cooler temp on the top of the stack
            while len(stack)>0 and stack[-1][0] < temp:
                coolerTemp = stack.pop()
                print(idx, coolerTemp[1])
                res[coolerTemp[1]] = idx-coolerTemp[1]

            # Add current days temp to stack
            stack.append((temp, idx))
        
        return res

