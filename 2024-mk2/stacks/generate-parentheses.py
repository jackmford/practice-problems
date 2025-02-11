
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def gen(s, openP, closedP):
            if openP == n and closedP == n:
                res.append(s)
                return
            
            if openP < n:
                s += "("
                gen(s, openP+1, closedP)
                s = s[:len(s)-1]
            if closedP < openP:
                s += ")"
                gen(s, openP, closedP+1)
                s = s[:len(s)-1]
            
            return
        
        gen("", 0, 0)
        return res
        
