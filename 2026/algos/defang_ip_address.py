class Solution:
    def defangIPaddr(self, address: str) -> str:
        parts = address.split(".")
        res = ""
        for i in range(len(parts) - 1):
            res += f"{parts[i]}[.]"

        res += parts[-1]

        return res
