class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        number = ""
        dig = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if digits == "":
            return []

        def dfs(i):
            nonlocal number
            if i == len(digits):
                res.append(number)
                return
            print(i, digits[i])
            for d in dig[digits[i]]:
                print(d)
                
                number+=(d)
                dfs(i+1)
                number=number[:-1]
        dfs(0)
        return res
