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
