class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i, j = 0, 1
        result = [0] * len(temperatures)

        while i < len(temperatures):
            if j >= len(temperatures):
                i += 1
                j = i + 1
                continue
            if temperatures[j] > temperatures[i]:
                result[i] = j - i
                i += 1
                j = i + 1
            else:
                j += 1

        return result

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]
                temp, index = stack.pop()
                res[index] = i - index
            stack.append((temperatures[i], i))
            
        return stack
            
