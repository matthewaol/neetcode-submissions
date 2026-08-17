class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # same as the count island problem, except for each bfs iteration, track the number of neighbors we have. store this as a global result
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        res = 0 

        visited = set()
        
        def bfs(r, c):
            nonlocal res
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            curr_island_area = 1

            while q:
                row, col = q.popleft()


                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r in range(rows) and c in range(cols) and (r, c) not in visited and grid[r][c] == 1:
                        visited.add((r, c))
                        q.append((r, c))
                        curr_island_area += 1

            res = max(res, curr_island_area)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    bfs(r, c)

        return res
        



