"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for i in range(len(words)):
            word = words[i]
            j = len(word)-1
            new_word = ""
            print(word)

            while j>=0:
                new_word += word[j]
                j-=1

            print(new_word)
            words[i] = new_word
        res = ""
        for i in range(len(words)):
            if i!=len(words)-1:
                res+=words[i]+" "
            else:
                res+=words[i]
        return res

sol = Solution()
print(sol.reverseWords("Let's take LeetCode contest"))
