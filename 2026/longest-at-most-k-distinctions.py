from collections import defaultdict


def longest_at_most_k_distinct(s, k):
    left = 0
    distinct = defaultdict(int)

    best = 0

    for right in range(len(s)):
        distinct[s[right]] += 1

        while len(distinct) > k:
            distinct[s[left]] -= 1

            if distinct[s[left]] == 0:
                distinct.pop(s[left])

            left += 1

        best = max(best, right - left + 1)

    return best


# grow window while distinct <= k
# shrink window while distinct > k

s = "eceba"
k = 2
print(longest_at_most_k_distinct(s, k))
