from typing import List
from collections import defaultdict

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        index = 2
        area = defaultdict(int)

        def dfs(i, j, idx):
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = idx
                res = 1
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    res += dfs(i + dx, j + dy, idx)
                return res
            return 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[index] = dfs(i, j, index)
                    index += 1

        result = max(area.values() or [0])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    total = 1
                    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            idx = grid[ni][nj]
                            if idx not in seen:
                                total += area[idx]
                                seen.add(idx)
                    result = max(result, total)

        return result
