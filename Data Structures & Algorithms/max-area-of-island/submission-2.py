class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # same as the count island problem, except for each bfs iteration, track the number of neighbors we have. store this as a global result
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        res = 1 
        area = 0 

        visited = set()
        
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            res = 1

            curr_island_area = 0
            while q:
                row, col = q.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if r in range(rows) and c in range(cols) and (r, c) not in visited and grid[r][c] == 1:
                        visited.add((r, c))
                        q.append((r, c))
                        res += 1

            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, bfs(r, c))

        return area

