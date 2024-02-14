class Solution:
    def addBinary(self, a: str, b: str) -> str:        
        carry = 0
        num = ""
        longest = min(len(a), len(b))
        a = a[::-1]
        b = b[::-1]
        if len(a) > len(b):
            for i in range(len(a)-len(b)):
                b+="0"
        elif len(b) > len(a):
            for i in range(len(b)-len(a)):
                a+="0"
        for i in range(len(a)):
            if a[i] == "1" and b[i] == "1" and carry == 0:
                num += "0"
                carry = 1
            elif a[i] == "1" and b[i] == "0" and carry == 0:
                num += "1"
            elif a[i] == "0" and b[i] == "1" and carry == 0:
                num += "1"
            elif a[i] == "0" and b[i] == "0" and carry == 0:
                num += "0"
            elif a[i] == "0" and b[i] == "0" and carry == 1:
                num += "1"
                carry = 0
            elif a[i] == "1" and b[i] == "0" and carry == 1:
                num += "0"
                carry = 1
            elif a[i] == "0" and b[i] == "1" and carry == 1:
                num += "0"
                carry = 1
            elif a[i] == "1" and b[i] == "1" and carry == 1:
                num += "1"
                carry = 1
        
   
        if carry == 1:
            num += "1"
        
        return num[::-1]         


class Solution:
    def addBinary(self, a: str, b: str) -> str:        
        num = ""
        carry = ""
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total%2)
            num += char + num
            carry = total // 2
        
        if carry:
            num = "1" + num
        return num