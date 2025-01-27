class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1

        for i in range(len(num)-2):
            sub = num[i:i+3]
            if sub[0] == sub[1] == sub[2]:
                res = max(res, int(sub))

        if res == 0:
            return "000"
        if res == -1:
            return ""
        return str(res)


