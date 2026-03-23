class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        keymap = {}
        keymap_two = {}

        for c in s:
            if c in keymap:
                keymap[c] += 1
            else:
                keymap[c] = 0

        for c in t:
            if c not in keymap:
                return False
            if c in keymap_two:
                keymap_two[c] += 1
            else:
                keymap_two[c] = 0

        for k in keymap.keys():
            if k not in keymap_two:
                return False
            if keymap[k] != keymap_two[k]:
                return False
        return True
