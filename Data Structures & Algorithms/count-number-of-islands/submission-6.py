class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 

        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        islands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0" # mark it as visited

            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if (nr < rows and nc < cols and nr >= 0 and nc >= 0 and grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        
        return islands