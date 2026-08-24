# 1. Sliding Window: Minimum Window Substring
# Given two strings s and t, return the smallest substring of s that contains every character in t, including duplicates.
# Example:
# s = "ADOBECODEBANC"
# t = "ABC"
# Expected answer:
# "BANC"
# Write:

from collections import defaultdict


def members(smap, tmap):
    for k in tmap.keys():
        if k not in smap:
            return False
        # i have less than I need, grow
        if smap[k] < tmap[k]:
            return False
    return True


def min_window(s, t):
    # while you have a valid window, shrink and shrink until it is invalid
    # grow while you have an invalid window
    # use something to compare chars in t to chars in window
    t_map = defaultdict(int)
    for c in t:
        t_map[c] += 1

    left = 0
    substring = ""
    s_map = defaultdict(int)

    for right in range(len(s)):
        s_map[s[right]] += 1
        while members(s_map, t_map):
            print(s[left : right + 1])
            if substring == "" or right - left + 1 < len(substring):
                substring = s[left : right + 1]
            s_map[s[left]] -= 1
            left += 1

    return substring


s = "ADOBECODEBANC"
t = "ABC"

print(min_window(s, t))
