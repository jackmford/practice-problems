class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    s_dict = {}
    t_dict = {}

    if len(s) != len(t):
      return False

    s = ''.join(sorted(s))
    t = ''.join(sorted(t))

    for i in range(len(s)):
      if s[i] != t[i]:
        return False

    return True

sol = Solution()
sol.isAnagram('hi', 'ihjasdf')
