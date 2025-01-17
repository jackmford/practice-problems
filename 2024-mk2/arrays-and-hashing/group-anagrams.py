class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        m = defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))
            m[sortedWord].append(word)

        for v in m.values():
            res.append(v)
        return res
            


