# 3. DFS/Grid: Number of Islands
# Given a 2D grid of "1"s and "0"s, return the number of islands.
# An island is a group of connected "1" cells connected horizontally or vertically.
# Example:
# grid = [
#     ["1", "1", "0", "0"],
#     ["1", "0", "0", "1"],
#     ["0", "0", "1", "1"],
# ]
# Expected answer:
# 2
# Write:


def num_islands(grid):
    seen = set()
    islands = 0

    def dfs(r, c):
        if r < 0 or r >= len(grid):
            return 0
        if c < 0 or c >= len(grid[0]):
            return 0
        if grid[r][c] == "0":
            return 0
        if (r, c) in seen:
            return 0

        seen.add((r, c))

        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)
        return 1

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1" and (r, c) not in seen:
                islands += dfs(r, c)

    return islands
