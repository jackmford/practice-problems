class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        for log in logs:
            split = log.split(" ", 1)
            identifier, content = split[0], split[1]
            if str.isdigit(content[0]):
                digits.append(log)
            else:
                letters.append((identifier, content, log))

        letters.sort(key=lambda x: (x[1], x[0]))
        final = [l[2] for l in letters]
        final.extend(digits)
        return final
