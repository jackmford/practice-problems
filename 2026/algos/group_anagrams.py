class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for w in strs:
            w_sort = "".join(sorted(w))
            d[w_sort].append(w)

        res = []
        for v in d.values():
            res.append(v)
        return res


# could use ord() operator like ord(char) - ord(a) and index by character index and not use sort
