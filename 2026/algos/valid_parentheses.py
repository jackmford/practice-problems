class Solution:
    def isValid(self, s: str) -> bool:
        # any time there is a closing pop
        closers = {")": "(", "}": "{", "]": "["}
        stack = []

        for i in range(len(s)):
            if len(stack) > 0 and s[i] in closers and stack[-1] == closers[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])

        if len(stack) > 0:
            return False
        return True
