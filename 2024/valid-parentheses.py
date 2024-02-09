class Solution:
    def isValid(self, s: str) -> bool:
        # use stack
        m = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in m and len(stack) > 0:
                if m[char] == stack[-1]:
                    stack.pop()
                else:
                   return False
            else:
                stack.append(char)
        
        if len(stack) == 0:
            return True

sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("(]"))
print(sol.isValid("()[]{}"))