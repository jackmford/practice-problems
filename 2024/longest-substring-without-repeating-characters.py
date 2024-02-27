class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmpStr = ''
        maxLen = 0

        for char in s:
            if char in tmpStr:
                for i in range(len(tmpStr)):
                    if tmpStr[i] == char:
                        tmpStr = tmpStr[i+1:]
                        break
            tmpStr += char
            if len(tmpStr) > maxLen:
                maxLen = len(tmpStr)
        
        return maxLen